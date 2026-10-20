# -*- coding: utf-8 -*-
"""
Dagim Info Tech — የትምህርት Telegram Bot
ትምህርቶች + ጥያቄዎች (Quiz) + AI አስተማሪ + ውጤት መከታተያ + ደረጃ ሰንጠረዥ
python-telegram-bot v21.4 · SQLite · Flask (Render keep-alive)
"""
import asyncio
import base64
import html
import logging
import os
import random
import sqlite3
import threading
from datetime import date

import httpx
from flask import Flask
from telegram import BotCommand
from telegram import InlineKeyboardButton as Btn
from telegram import InlineKeyboardMarkup as Kb
from telegram import Update
from telegram.constants import ChatAction, ParseMode
from telegram.error import BadRequest, TelegramError
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from content import CATEGORIES, LESSONS, QUIZ

# ───────────── ቅንብሮች (Environment Variables) ─────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
ADMIN_ID = int(os.environ.get("ADMIN_ID", "0") or 0)
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
AI_MODEL = os.environ.get("AI_MODEL", "claude-haiku-5-5").strip()
DAILY_AI_LIMIT = int(os.environ.get("DAILY_AI_LIMIT", "20") or 20)
CHANNEL = os.environ.get("CHANNEL_USERNAME", "").strip().lstrip("@")
DB_PATH = os.environ.get("DB_PATH", "edubot.db")

QUIZ_LEN = 5
POINTS_LESSON = 5
POINTS_CORRECT = 10
LETTERS = ["ሀ", "ለ", "ሐ", "መ", "ሠ", "ረ"]

AI_SYSTEM = (
    "You are a friendly, patient AI tutor inside the Dagim Info Tech education Telegram bot. "
    "Students are Ethiopian: school subjects for grades 9-12, technology and computer skills, "
    "and English language learning. Reply in the language the student writes in (default: Amharic). "
    "Explain simply with short examples, and step by step for math and science. "
    "The student may also send a photo of homework or a textbook problem. Read it carefully; "
    "if it is blurry or unreadable, politely ask for a clearer photo. Solve step by step and explain "
    "the method so the student learns, then state the final answer clearly. "
    "Keep answers under about 1500 characters. Use plain text only, with no Markdown symbols "
    "such as ** or #, because Telegram will show them raw. "
    "If the student seems to want homework simply done for them, guide them to understand it instead. "
    "If you are not sure about something, say so rather than guessing. Stay on educational topics."
)

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s", level=logging.INFO
)
log = logging.getLogger("edubot")

# ───────────── Flask (Render ላይ እንዳይተኛ) ─────────────
web = Flask(__name__)


@web.route("/")
def home():
    return "Edu bot is running ✅"


def run_web():
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


# ───────────── Database ─────────────
_lock = threading.Lock()


def db(sql, params=(), fetch=None):
    with _lock:
        con = sqlite3.connect(DB_PATH)
        try:
            cur = con.execute(sql, params)
            if fetch == "all":
                out = cur.fetchall()
            elif fetch == "one":
                out = cur.fetchone()
            else:
                out = cur.rowcount
            con.commit()
            return out
        finally:
            con.close()


def init_db():
    db(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            joined TEXT DEFAULT CURRENT_TIMESTAMP,
            points INTEGER DEFAULT 0,
            ai_date TEXT DEFAULT '',
            ai_count INTEGER DEFAULT 0)"""
    )
    db(
        """CREATE TABLE IF NOT EXISTS progress (
            user_id INTEGER, cat TEXT, idx INTEGER,
            ts TEXT DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, cat, idx))"""
    )
    db(
        """CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER, cat TEXT, score INTEGER, total INTEGER,
            ts TEXT DEFAULT CURRENT_TIMESTAMP)"""
    )


def upsert_user(u):
    name = (u.full_name or "ተማሪ")[:60]
    uname = u.username or ""
    db("INSERT OR IGNORE INTO users (id, name, username) VALUES (?,?,?)", (u.id, name, uname))
    db("UPDATE users SET name=?, username=? WHERE id=?", (name, uname, u.id))


def add_points(uid, n):
    db("UPDATE users SET points = points + ? WHERE id=?", (n, uid))


def take_ai_quota(uid):
    today = date.today().isoformat()
    row = db("SELECT ai_date, ai_count FROM users WHERE id=?", (uid,), "one")
    d, c = row if row else ("", 0)
    if d != today:
        c = 0
    if c >= DAILY_AI_LIMIT:
        return False
    db("UPDATE users SET ai_date=?, ai_count=? WHERE id=?", (today, c + 1, uid))
    return True


# ───────────── Helpers ─────────────
async def show(q, text, kb=None):
    """ያለውን መልእክት አስተካክል (ተመሳሳይ ከሆነ ስህተት አይሰጥም)።"""
    try:
        await q.edit_message_text(text, reply_markup=kb, parse_mode=ParseMode.HTML)
    except BadRequest as e:
        if "not modified" not in str(e).lower():
            raise


def split_text(text, n=4000):
    return [text[i : i + n] for i in range(0, len(text), n)] or [""]


def main_kb():
    return Kb(
        [
            [Btn("📚 ትምህርቶች", callback_data="learn"), Btn("🧠 ጥያቄዎች", callback_data="quiz")],
            [Btn("🤖 AI አስተማሪ", callback_data="ai"), Btn("📸 የቤት ሥራ ፎቶ", callback_data="hw")],
            [Btn("📊 ውጤቴ", callback_data="stats"), Btn("🏆 ደረጃ", callback_data="top")],
            [Btn("ℹ️ ስለ bot-ኡ", callback_data="about")],
        ]
    )


def home_btn():
    return [Btn("🏠 ዋና ምናሌ", callback_data="menu")]


def cat_kb(prefix, back="menu"):
    rows = [[Btn(name, callback_data=f"{prefix}:{key}")] for key, name in CATEGORIES.items()]
    rows.append([Btn("⬅️ ተመለስ", callback_data=back)])
    return Kb(rows)


def ai_kb():
    return Kb([[Btn("🔚 ከ AI አስተማሪ ውጣ", callback_data="aioff")]])


def welcome_text(name):
    return (
        f"👋 ሰላም <b>{html.escape(name)}</b>!\n\n"
        "እንኳን ወደ <b>የትምህርት bot</b> በደህና መጡ። እዚህ፦\n"
        "📚 አጫጭር ትምህርቶችን ታነባለህ\n"
        "🧠 ጥያቄዎችን ሠርተህ ነጥብ ትሰበስባለህ\n"
        "🤖 ማንኛውንም ጥያቄ AI አስተማሪን ትጠይቃለህ\n"
        "📸 የቤት ሥራህን ፎቶ አንስተህ ትልካለህ፤ ደረጃ በደረጃ ያስረዳሃል\n\n"
        "ከታች ይምረጡ 👇"
    )


# ───────────── Commands ─────────────
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    upsert_user(u)
    ctx.user_data.clear()
    await update.message.reply_text(
        welcome_text(u.first_name or "ተማሪ"), reply_markup=main_kb(), parse_mode=ParseMode.HTML
    )


async def cmd_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    upsert_user(update.effective_user)
    ctx.user_data.pop("quiz", None)
    ctx.user_data.pop("ai", None)
    await update.message.reply_text("🏠 ዋና ምናሌ", reply_markup=main_kb())


async def cmd_stop(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.pop("ai", None)
    await update.message.reply_text("✅ ከ AI አስተማሪ ወጥተሃል።", reply_markup=main_kb())


# ───────────── ትምህርቶች ─────────────
def lesson_view(uid, cat, idx):
    items = LESSONS[cat]
    idx = max(0, min(idx, len(items) - 1))
    item = items[idx]
    is_new = db(
        "INSERT OR IGNORE INTO progress (user_id, cat, idx) VALUES (?,?,?)", (uid, cat, idx)
    ) > 0
    if is_new:
        add_points(uid, POINTS_LESSON)
    text = f"📘 <b>{html.escape(item['title'])}</b>  ({idx + 1}/{len(items)})\n\n{item['body']}"
    if is_new:
        text += f"\n\n⭐ +{POINTS_LESSON} ነጥብ አግኝተሃል!"
    nav = []
    if idx > 0:
        nav.append(Btn("⬅️ ቀዳሚ", callback_data=f"ll:{cat}:{idx - 1}"))
    if idx < len(items) - 1:
        nav.append(Btn("ቀጣይ ➡️", callback_data=f"ll:{cat}:{idx + 1}"))
    rows = [nav] if nav else []
    rows.append(
        [Btn("📋 ዝርዝር", callback_data=f"lc:{cat}"), Btn("🧠 ጥያቄ ሞክር", callback_data=f"qs:{cat}")]
    )
    rows.append(home_btn())
    return text, Kb(rows)


# ───────────── ጥያቄዎች (Quiz) ─────────────
def question_text(quiz):
    pos = quiz["pos"]
    item = QUIZ[quiz["cat"]][quiz["qs"][pos]]
    return (
        f"🧠 <b>ጥያቄ {pos + 1}/{len(quiz['qs'])}</b> · {CATEGORIES[quiz['cat']]}\n\n"
        f"{html.escape(item['q'])}"
    )


def question_view(quiz):
    pos = quiz["pos"]
    item = QUIZ[quiz["cat"]][quiz["qs"][pos]]
    order = quiz["orders"][pos]
    rows = [
        [Btn(f"{LETTERS[j]}) {item['options'][o]}", callback_data=f"qa:{pos}:{j}")]
        for j, o in enumerate(order)
    ]
    return question_text(quiz), Kb(rows)


async def quiz_start(q, ctx, cat):
    n = len(QUIZ[cat])
    chosen = random.sample(range(n), min(QUIZ_LEN, n))
    orders = []
    for i in chosen:
        k = len(QUIZ[cat][i]["options"])
        orders.append(random.sample(range(k), k))
    ctx.user_data["quiz"] = {
        "cat": cat,
        "qs": chosen,
        "orders": orders,
        "pos": 0,
        "score": 0,
        "answered": False,
    }
    text, kb = question_view(ctx.user_data["quiz"])
    await show(q, text, kb)


async def quiz_answer(q, ctx, pos, choice):
    quiz = ctx.user_data.get("quiz")
    if not quiz or quiz["pos"] != pos or quiz.get("answered"):
        await q.answer("ይህ ጥያቄ አልቋል። እንደገና ጀምር 🔄", show_alert=True)
        return
    await q.answer()
    item = QUIZ[quiz["cat"]][quiz["qs"][pos]]
    order = quiz["orders"][pos]
    if not 0 <= choice < len(order):
        return
    ok = order[choice] == item["answer"]
    quiz["answered"] = True
    if ok:
        quiz["score"] += 1
        verdict = "✅ <b>ትክክል!</b>"
    else:
        right = html.escape(item["options"][item["answer"]])
        verdict = f"❌ <b>ስህተት።</b> ትክክለኛው መልስ፦ <b>{right}</b>"
    text = f"{question_text(quiz)}\n\n{verdict}\n💡 {html.escape(item['explain'])}"
    last = pos + 1 >= len(quiz["qs"])
    label = "🏁 ውጤት ተመልከት" if last else "ቀጣይ ጥያቄ ➡️"
    await show(q, text, Kb([[Btn(label, callback_data="qn")]]))


async def quiz_next(q, ctx, uid):
    quiz = ctx.user_data.get("quiz")
    if not quiz or not quiz.get("answered"):
        await show(q, "🏠 ዋና ምናሌ", main_kb())
        return
    quiz["pos"] += 1
    quiz["answered"] = False
    if quiz["pos"] >= len(quiz["qs"]):
        await quiz_finish(q, ctx, uid)
    else:
        text, kb = question_view(quiz)
        await show(q, text, kb)


async def quiz_finish(q, ctx, uid):
    quiz = ctx.user_data.pop("quiz", None)
    if not quiz:
        return
    score, total = quiz["score"], len(quiz["qs"])
    gained = score * POINTS_CORRECT
    db(
        "INSERT INTO quiz_results (user_id, cat, score, total) VALUES (?,?,?,?)",
        (uid, quiz["cat"], score, total),
    )
    add_points(uid, gained)
    if score == total:
        msg = "🏆 ድንቅ! ሁሉንም ትክክል መለስህ!"
    elif score >= total * 0.6:
        msg = "👏 ጥሩ ነው! ትንሽ ልምምድ ይበቃል።"
    else:
        msg = "📖 አትዘን፤ ትምህርቶቹን ደግመህ አንብበህ ሞክር።"
    text = (
        f"🏁 <b>ጥያቄው አብቅቷል!</b>\n\n"
        f"{CATEGORIES[quiz['cat']]}\n"
        f"ውጤት፦ <b>{score}/{total}</b>\n"
        f"⭐ +{gained} ነጥብ\n\n{msg}"
    )
    kb = Kb(
        [
            [Btn("🔄 እንደገና", callback_data=f"qs:{quiz['cat']}")],
            [Btn("📚 ትምህርቶች", callback_data=f"lc:{quiz['cat']}")],
            home_btn(),
        ]
    )
    await show(q, text, kb)


# ───────────── ውጤት እና ደረጃ ─────────────
def stats_text(uid):
    row = db("SELECT points FROM users WHERE id=?", (uid,), "one")
    points = row[0] if row else 0
    rank = db("SELECT COUNT(*) + 1 FROM users WHERE points > ?", (points,), "one")[0]
    lines = [f"📊 <b>የእኔ ውጤት</b>\n\n⭐ ነጥብ፦ <b>{points}</b>\n🏅 ደረጃ፦ <b>{rank}ኛ</b>\n\n<b>📚 ትምህርቶች</b>"]
    for key, name in CATEGORIES.items():
        done = db("SELECT COUNT(*) FROM progress WHERE user_id=? AND cat=?", (uid, key), "one")[0]
        lines.append(f"{name}፦ {done}/{len(LESSONS[key])}")
    n, s, t = db(
        "SELECT COUNT(*), COALESCE(SUM(score),0), COALESCE(SUM(total),0) FROM quiz_results WHERE user_id=?",
        (uid,),
        "one",
    )
    acc = round(100 * s / t) if t else 0
    lines.append(f"\n<b>🧠 ጥያቄዎች</b>\nየሞከርካቸው፦ {n}\nትክክለኝነት፦ {acc}%")
    return "\n".join(lines)


def top_text():
    rows = db("SELECT name, points FROM users WHERE points > 0 ORDER BY points DESC LIMIT 10", fetch="all")
    if not rows:
        return "🏆 <b>ደረጃ ሰንጠረዥ</b>\n\nእስካሁን ማንም ነጥብ አልሰበሰበም። የመጀመሪያው ሁን! 💪"
    medals = ["🥇", "🥈", "🥉"] + ["▫️"] * 7
    lines = ["🏆 <b>ደረጃ ሰንጠረዥ — ምርጥ 10</b>\n"]
    for i, (name, pts) in enumerate(rows):
        lines.append(f"{medals[i]} {html.escape(name)} — <b>{pts}</b>")
    return "\n".join(lines)


# ───────────── AI አስተማሪ ─────────────
async def ask_ai(messages):
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": AI_MODEL,
                "max_tokens": 1200,
                "system": AI_SYSTEM,
                "messages": messages,
            },
        )
        r.raise_for_status()
        data = r.json()
    return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text").strip()


async def on_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    upsert_user(u)
    text = (update.message.text or "").strip()
    if not ctx.user_data.get("ai"):
        await update.message.reply_text(
            "👇 ከምናሌው ይምረጡ። AI አስተማሪን ለመጠየቅ «🤖 AI አስተማሪ» ይጫኑ።", reply_markup=main_kb()
        )
        return
    if not take_ai_quota(u.id):
        await update.message.reply_text(
            f"⏳ የዛሬው {DAILY_AI_LIMIT} ጥያቄ ተጠናቅቋል። ነገ ተመልሰው ይሞክሩ!", reply_markup=ai_kb()
        )
        return
    await ctx.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)
    hist = ctx.user_data.setdefault("ai_hist", [])
    hist.append({"role": "user", "content": text[:2000]})
    del hist[:-8]
    while hist and hist[0]["role"] != "user":
        hist.pop(0)
    try:
        answer = await ask_ai(hist)
    except Exception:
        log.exception("AI error")
        hist.pop()
        await update.message.reply_text(
            "⚠️ ይቅርታ፣ አሁን መመለስ አልቻልኩም። ትንሽ ቆይተው ይሞክሩ።", reply_markup=ai_kb()
        )
        return
    if not answer:
        answer = "ይቅርታ፣ መልስ ማዘጋጀት አልቻልኩም። ጥያቄውን በሌላ መንገድ ይጠይቁ።"
    hist.append({"role": "assistant", "content": answer})
    chunks = split_text(answer)
    for i, chunk in enumerate(chunks):
        await update.message.reply_text(chunk, reply_markup=ai_kb() if i == len(chunks) - 1 else None)


async def on_photo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """የቤት ሥራ ፎቶ ተቀብሎ በ AI ይመልሳል።"""
    u = update.effective_user
    upsert_user(u)
    msg = update.message
    if not ANTHROPIC_API_KEY:
        await msg.reply_text("📸 የፎቶ ትንተና ለጊዜው አልነቃም።", reply_markup=main_kb())
        return
    if not take_ai_quota(u.id):
        await msg.reply_text(
            f"⏳ የዛሬው {DAILY_AI_LIMIT} ጥያቄ ተጠናቅቋል። ነገ ተመልሰው ይሞክሩ!", reply_markup=main_kb()
        )
        return
    photo = None
    for p in sorted(msg.photo, key=lambda x: x.width * x.height, reverse=True):
        if (p.file_size or 0) <= 4_500_000:
            photo = p
            break
    if photo is None:
        await msg.reply_text("⚠️ ፎቶው በጣም ትልቅ ነው። ትንሽ ቀንሰህ ላክ።")
        return
    await ctx.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)
    caption = (msg.caption or "").strip()[:500]
    prompt = caption or "ይህን የቤት ሥራ ፎቶ በጥንቃቄ አንብብ። ጥያቄዎቹን ለይተህ ደረጃ በደረጃ በማስረዳት መልስ።"
    hist = ctx.user_data.setdefault("ai_hist", [])
    try:
        tg_file = await photo.get_file()
        raw = await tg_file.download_as_bytearray()
        b64 = base64.b64encode(bytes(raw)).decode()
        messages = hist[-6:] + [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {"type": "base64", "media_type": "image/jpeg", "data": b64},
                    },
                    {"type": "text", "text": prompt},
                ],
            }
        ]
        while messages and messages[0]["role"] != "user":
            messages.pop(0)
        answer = await ask_ai(messages)
    except Exception:
        log.exception("Photo AI error")
        await msg.reply_text(
            "⚠️ ይቅርታ፣ ፎቶውን ማንበብ አልቻልኩም። ግልጽ እና በቂ ብርሃን ያለው ፎቶ እንደገና ላክ።",
            reply_markup=main_kb(),
        )
        return
    if not answer:
        answer = "ይቅርታ፣ ከፎቶው መልስ ማዘጋጀት አልቻልኩም። ግልጽ ፎቶ እንደገና ላክ።"
    hist.append({"role": "user", "content": "[የቤት ሥራ ፎቶ] " + prompt})
    hist.append({"role": "assistant", "content": answer})
    del hist[:-8]
    while hist and hist[0]["role"] != "user":
        hist.pop(0)
    ctx.user_data["ai"] = True  # ተከታታይ ጥያቄ መጠየቅ እንዲችል
    chunks = split_text(answer)
    for i, chunk in enumerate(chunks):
        await msg.reply_text(chunk, reply_markup=ai_kb() if i == len(chunks) - 1 else None)


# ───────────── Callback router ─────────────
async def on_cb(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    parts = (q.data or "").split(":")
    cmd = parts[0]
    uid = q.from_user.id
    upsert_user(q.from_user)
    if cmd != "qa":
        await q.answer()

    if cmd == "menu":
        ctx.user_data.pop("quiz", None)
        ctx.user_data.pop("ai", None)
        await show(q, welcome_text(q.from_user.first_name or "ተማሪ"), main_kb())

    elif cmd == "learn":
        await show(q, "📚 <b>ትምህርቶች</b>\n\nርዕስ ይምረጡ፦", cat_kb("lc"))

    elif cmd == "lc" and len(parts) > 1 and parts[1] in CATEGORIES:
        cat = parts[1]
        viewed = {
            r[0]
            for r in db("SELECT idx FROM progress WHERE user_id=? AND cat=?", (uid, cat), "all")
        }
        rows = [
            [Btn(f"{'✅' if i in viewed else '📘'} {it['title']}", callback_data=f"ll:{cat}:{i}")]
            for i, it in enumerate(LESSONS[cat])
        ]
        rows.append([Btn("⬅️ ተመለስ", callback_data="learn")])
        await show(q, f"{CATEGORIES[cat]}\n\nትምህርት ይምረጡ፦", Kb(rows))

    elif cmd == "ll" and len(parts) > 2 and parts[1] in CATEGORIES:
        try:
            idx = int(parts[2])
        except ValueError:
            return
        text, kb = lesson_view(uid, parts[1], idx)
        await show(q, text, kb)

    elif cmd == "quiz":
        await show(q, "🧠 <b>ጥያቄዎች</b>\n\nርዕስ ይምረጡ (5 ጥያቄዎች)፦", cat_kb("qs"))

    elif cmd == "qs" and len(parts) > 1 and parts[1] in CATEGORIES:
        await quiz_start(q, ctx, parts[1])

    elif cmd == "qa" and len(parts) > 2:
        try:
            await quiz_answer(q, ctx, int(parts[1]), int(parts[2]))
        except ValueError:
            await q.answer()

    elif cmd == "qn":
        await quiz_next(q, ctx, uid)

    elif cmd == "ai":
        if not ANTHROPIC_API_KEY:
            await show(
                q,
                "🤖 AI አስተማሪ ለጊዜው አልነቃም።\nእስከዚያው ትምህርቶችንና ጥያቄዎችን ይጠቀሙ።",
                Kb([home_btn()]),
            )
        else:
            ctx.user_data["ai"] = True
            ctx.user_data["ai_hist"] = []
            await show(
                q,
                "🤖 <b>AI አስተማሪ</b>\n\nማንኛውንም የትምህርት ጥያቄ ይጻፉ — በአማርኛ ወይም በእንግሊዝኛ።\n"
                f"በቀን እስከ {DAILY_AI_LIMIT} ጥያቄ።\n\nለመውጣት ከታች ይጫኑ ወይም /stop ይላኩ።",
                ai_kb(),
            )

    elif cmd == "hw":
        if not ANTHROPIC_API_KEY:
            await show(q, "📸 የፎቶ ትንተና ለጊዜው አልነቃም።", Kb([home_btn()]))
        else:
            ctx.user_data["ai"] = True
            ctx.user_data["ai_hist"] = []
            await show(
                q,
                "📸 <b>የቤት ሥራ ፎቶ</b>\n\nየቤት ሥራህን ወይም የመጽሐፍ ጥያቄ ፎቶ አንስተህ እዚህ ላክ።\n\n"
                "💡 ጠቃሚ ምክሮች፦\n• ጥሩ ብርሃን ይኑር\n• ጽሁፉ ግልጽ እና ቀጥ ያለ ይሁን\n"
                "• አንድ ጊዜ አንድ ጥያቄ ቢሆን ይሻላል\n• ከፈለግህ ከፎቶው ጋር መግለጫ (caption) ጻፍ\n\n"
                "ለመውጣት ከታች ይጫኑ።",
                ai_kb(),
            )

    elif cmd == "aioff":
        ctx.user_data.pop("ai", None)
        await show(q, welcome_text(q.from_user.first_name or "ተማሪ"), main_kb())

    elif cmd == "stats":
        await show(q, stats_text(uid), Kb([home_btn()]))

    elif cmd == "top":
        await show(q, top_text(), Kb([home_btn()]))

    elif cmd == "about":
        rows = []
        if CHANNEL:
            rows.append([Btn("📢 ቻናላችን", url=f"https://t.me/{CHANNEL}")])
        rows.append(home_btn())
        await show(
            q,
            "ℹ️ <b>ስለ bot-ኡ</b>\n\nበ <b>Dagim Info Tech</b> የተሠራ የአማርኛ የትምህርት bot።\n"
            "ትምህርት ቤት (9-12)፣ ቴክኖሎጂ እና እንግሊዝኛ ቋንቋ።\n"
            "📸 የቤት ሥራ ፎቶ ተቀብሎ ያስረዳል።\n\n"
            f"⭐ ትምህርት ማንበብ = +{POINTS_LESSON} ነጥብ\n"
            f"⭐ ትክክለኛ መልስ = +{POINTS_CORRECT} ነጥብ",
            Kb(rows),
        )


# ───────────── Admin ─────────────
def is_admin(update: Update):
    return bool(ADMIN_ID) and update.effective_user.id == ADMIN_ID


async def cmd_stats(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return
    users = db("SELECT COUNT(*) FROM users", fetch="one")[0]
    lessons = db("SELECT COUNT(*) FROM progress", fetch="one")[0]
    quizzes = db("SELECT COUNT(*) FROM quiz_results", fetch="one")[0]
    ai_today = db(
        "SELECT COALESCE(SUM(ai_count),0) FROM users WHERE ai_date=?",
        (date.today().isoformat(),),
        "one",
    )[0]
    await update.message.reply_text(
        f"📈 Bot Stats\n\n👥 ተጠቃሚዎች፦ {users}\n📘 የተነበቡ ትምህርቶች፦ {lessons}\n"
        f"🧠 የተሠሩ ጥያቄዎች፦ {quizzes}\n🤖 የዛሬ AI ጥያቄዎች፦ {ai_today}"
    )


async def cmd_broadcast(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return
    parts = (update.message.text or "").split(maxsplit=1)
    if len(parts) < 2:
        await update.message.reply_text("አጠቃቀም፦ /broadcast መልእክትህ እዚህ")
        return
    ids = [r[0] for r in db("SELECT id FROM users", fetch="all")]
    ok = fail = 0
    for uid in ids:
        try:
            await ctx.bot.send_message(uid, parts[1])
            ok += 1
        except TelegramError:
            fail += 1
        await asyncio.sleep(0.05)
    await update.message.reply_text(f"✅ ተልኳል፦ {ok}\n❌ አልተላከም፦ {fail}")


async def on_error(update, ctx: ContextTypes.DEFAULT_TYPE):
    log.error("Update error", exc_info=ctx.error)


# ───────────── Main ─────────────
async def post_init(app: Application):
    await app.bot.set_my_commands(
        [
            BotCommand("start", "ጀምር"),
            BotCommand("menu", "ዋና ምናሌ"),
            BotCommand("stop", "ከ AI አስተማሪ ውጣ"),
        ]
    )


def main():
    if not BOT_TOKEN:
        raise SystemExit("❌ BOT_TOKEN አልተሞላም። README.md ን ይመልከቱ።")
    init_db()
    if os.environ.get("PORT"):
        threading.Thread(target=run_web, daemon=True).start()

    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("menu", cmd_menu))
    app.add_handler(CommandHandler("stop", cmd_stop))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("broadcast", cmd_broadcast))
    app.add_handler(CallbackQueryHandler(on_cb))
    app.add_handler(MessageHandler(filters.PHOTO, on_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(on_error)
    log.info("Bot started ✅")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
