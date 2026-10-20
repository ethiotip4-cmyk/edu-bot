# -*- coding: utf-8 -*-
"""
English ትምህርቶች እና ጥያቄዎች — ከ1ኛ እስከ 12ኛ ክፍል።
ህግ፦ body ውስጥ <b>ደማቅ</b> ብቻ። "<" ወይም "&" ምልክት አትጠቀም።
answer = የትክክለኛው አማራጭ ቁጥር (ከ 0 ይጀምራል)።
"""

ENGLISH_PACKS = {
    # ───────────────────────── 1ኛ - 4ኛ ክፍል ─────────────────────────
    "eng_1_4": {
        "title": "🇬🇧 English · 1ኛ-4ኛ ክፍል",
        "lessons": [
            {
                "title": "ፊደላት (The Alphabet)",
                "body": (
                    "እንግሊዝኛ <b>26 ፊደላት</b> አሉት፦\nA B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n\n"
                    "<b>Vowels (አናባቢዎች)፦</b> a, e, i, o, u\n"
                    "ሌሎቹ ሁሉ <b>Consonants (ተነባቢዎች)</b> ናቸው።\n\n"
                    "<b>ምሳሌ፦</b>\nA — Apple · B — Ball · C — Cat · D — Dog"
                ),
            },
            {
                "title": "ስሞች እና a / an (Nouns)",
                "body": (
                    "<b>Noun</b> የሰው፣ የእንስሳ፣ የቦታ ወይም የነገር ስም ነው፦ boy, dog, school, book\n\n"
                    "<b>a / an</b> (አንድ)፦\n"
                    "• a + ተነባቢ ድምጽ → a book, a dog\n"
                    "• an + አናባቢ ድምጽ → an apple, an egg\n\n"
                    "<b>ብዙ ቁጥር (Plural)፦</b>\n"
                    "book → books · box → boxes\nchild → children · man → men"
                ),
            },
            {
                "title": "Pronouns እና to be",
                "body": (
                    "<b>Pronouns (ተውላጠ ስም)፦</b> I, you, he, she, it, we, they\n\n"
                    "<b>to be፦</b>\n"
                    "I <b>am</b> a student.\n"
                    "He / She / It <b>is</b> a teacher.\n"
                    "You / We / They <b>are</b> friends.\n\n"
                    "<b>አሉታዊ፦</b> I am not · She is not · They are not"
                ),
            },
            {
                "title": "Action Verbs (ድርጊት ቃላት)",
                "body": (
                    "<b>Verb</b> ድርጊትን ይገልጻል፦ run, eat, write, read, play\n\n"
                    "I / You / We / They + verb → I <b>eat</b> injera.\n"
                    "He / She / It + verb<b>s</b> → She <b>eats</b> injera.\n\n"
                    "<b>አሉታዊ፦</b> do not (don't) · does not (doesn't)\n"
                    "I don't eat meat. He doesn't run."
                ),
            },
            {
                "title": "ቀለማት፣ ቁጥሮች እና ተቃራኒዎች",
                "body": (
                    "<b>Colours፦</b> red (ቀይ) · blue (ሰማያዊ) · green (አረንጓዴ) · yellow (ቢጫ) · black (ጥቁር) · white (ነጭ)\n\n"
                    "<b>Numbers፦</b> 1 one · 2 two · 3 three · 4 four · 5 five · 6 six · 7 seven · 8 eight · 9 nine · 10 ten\n\n"
                    "<b>Opposites፦</b> big ↔ small · tall ↔ short · hot ↔ cold · happy ↔ sad · open ↔ close"
                ),
            },
        ],
        "quiz": [
            {"q": "ከሚከተሉት ውስጥ vowel (አናባቢ) የቱ ነው?", "options": ["b", "a", "c", "d"], "answer": 1,
             "explain": "Vowels: a, e, i, o, u።"},
            {"q": "___ apple", "options": ["a", "an", "two", "is"], "answer": 1,
             "explain": "ከአናባቢ ድምጽ በፊት an ይመጣል።"},
            {"q": "የ «book» ብዙ ቁጥር የቱ ነው?", "options": ["bookes", "books", "bookies", "book"], "answer": 1,
             "explain": "አብዛኛዎቹ ስሞች ላይ s ይጨመራል።"},
            {"q": "I ___ a student.", "options": ["is", "are", "am", "be"], "answer": 2,
             "explain": "ከ I ጋር am ይሄዳል።"},
            {"q": "She ___ milk every morning.", "options": ["drink", "drinks", "drinking", "drank"], "answer": 1,
             "explain": "ከ He/She/It ጋር በ Present Simple verb ላይ s ይጨመራል።"},
            {"q": "«Red» ማለት ምን ማለት ነው?", "options": ["ሰማያዊ", "ቀይ", "ጥቁር", "ነጭ"], "answer": 1,
             "explain": "red = ቀይ።"},
            {"q": "የ «big» ተቃራኒ የቱ ነው?", "options": ["tall", "small", "hot", "old"], "answer": 1,
             "explain": "big ↔ small።"},
            {"q": "They ___ my friends.", "options": ["is", "am", "are", "be"], "answer": 2,
             "explain": "ከ They ጋር are ይሄዳል።"},
            {"q": "የ «child» ብዙ ቁጥር የቱ ነው?", "options": ["childs", "children", "childes", "childrens"], "answer": 1,
             "explain": "child → children (ልዩ ብዙ ቁጥር)።"},
            {"q": "He ___ not like tea.", "options": ["do", "does", "is", "are"], "answer": 1,
             "explain": "ከ He/She/It ጋር በአሉታዊ ዓረፍተ ነገር does not ይጠቀማል።"},
        ],
    },
    # ───────────────────────── 5ኛ - 6ኛ ክፍል ─────────────────────────
    "eng_5_6": {
        "title": "🇬🇧 English · 5ኛ-6ኛ ክፍል",
        "lessons": [
            {
                "title": "Present Simple እና Present Continuous",
                "body": (
                    "<b>Present Simple</b> — ልማድ እና እውነታ፦\n"
                    "She <b>plays</b> football every Sunday.\n"
                    "ምልክቶች፦ every day, always, usually, often\n\n"
                    "<b>Present Continuous</b> — አሁን እየሆነ ያለ፦\n"
                    "She <b>is playing</b> football now.\n"
                    "ቅርጽ፦ am / is / are + verb-ing\n"
                    "ምልክቶች፦ now, at the moment, Look!"
                ),
            },
            {
                "title": "Past Simple (ያለፈ ጊዜ)",
                "body": (
                    "<b>Regular verbs</b> + ed፦ play → played · walk → walked\n\n"
                    "<b>Irregular verbs</b>፦\n"
                    "go → went · eat → ate · see → saw\n"
                    "buy → bought · have → had · come → came\n\n"
                    "<b>አሉታዊ፦</b> did not (didn't) + verb\nI didn't go to school yesterday.\n\n"
                    "<b>ጥያቄ፦</b> Did you go? — Yes, I did."
                ),
            },
            {
                "title": "Future: will እና going to",
                "body": (
                    "<b>will + verb</b> — ድንገተኛ ውሳኔ ወይም ግምት፦\n"
                    "I will help you. · It will rain tomorrow.\n\n"
                    "<b>am / is / are going to + verb</b> — አስቀድሞ የታቀደ፦\n"
                    "I am going to visit my aunt next week.\n\n"
                    "<b>አሉታዊ፦</b> will not (won't) · am/is/are not going to"
                ),
            },
            {
                "title": "Adjectives እና Comparison",
                "body": (
                    "<b>አጭር ቃላት</b> (er / est)፦\ntall → taller → tallest\nbig → bigger → biggest\n\n"
                    "<b>ረጅም ቃላት</b> (more / most)፦\nbeautiful → more beautiful → most beautiful\n\n"
                    "<b>ልዩ ቃላት</b>፦\ngood → better → best\nbad → worse → worst\n\n"
                    "<b>as ... as</b> (እኩል)፦ He is as tall as me."
                ),
            },
            {
                "title": "Prepositions (መስተዋድዶች)",
                "body": (
                    "<b>ጊዜ፦</b>\nat 5 o'clock · on Monday · in June · in 2020\n\n"
                    "<b>ቦታ፦</b>\nat school · on the table · in the box\n\n"
                    "<b>ሌሎች፦</b> under (ከስር) · between (መካከል) · next to (አጠገብ) · behind (ከኋላ) · in front of (ከፊት)"
                ),
            },
            {
                "title": "Question Words (መጠይቅ ቃላት)",
                "body": (
                    "<b>What</b> — ምን · <b>Where</b> — የት · <b>When</b> — መቼ\n"
                    "<b>Who</b> — ማን · <b>Why</b> — ለምን · <b>How</b> — እንዴት\n"
                    "<b>How many</b> — ስንት (ሊቆጠር የሚችል) · <b>How much</b> — ስንት (ዋጋ ወይም መጠን)\n\n"
                    "<b>ምሳሌ፦</b>\nWhere do you live?\nWhat is your name?\nHow many books do you have?"
                ),
            },
        ],
        "quiz": [
            {"q": "She ___ to school every day.", "options": ["go", "goes", "going", "is go"], "answer": 1,
             "explain": "ልማድ ስለሆነ Present Simple፤ ከ She ጋር goes።"},
            {"q": "Look! The children ___ football now.", "options": ["play", "plays", "are playing", "played"], "answer": 2,
             "explain": "«Look!» እና «now» ምልክቶች → Present Continuous።"},
            {"q": "Yesterday I ___ to the market.", "options": ["go", "goes", "went", "going"], "answer": 2,
             "explain": "go ልዩ ግስ ነው፤ ያለፈው ቅርጹ went።"},
            {"q": "I ___ visit my uncle next week. I have already bought the ticket.",
             "options": ["will", "am going to", "went", "visit"], "answer": 1,
             "explain": "አስቀድሞ የታቀደ ድርጊት → be going to።"},
            {"q": "የ «tall» comparative ቅርጽ የቱ ነው?", "options": ["more tall", "taller", "tallest", "tallier"], "answer": 1,
             "explain": "አጭር ቃል + er → taller።"},
            {"q": "የ «good» superlative ቅርጽ የቱ ነው?", "options": ["gooder", "better", "best", "most good"], "answer": 2,
             "explain": "good → better → best (ልዩ)።"},
            {"q": "The meeting is ___ Monday.", "options": ["in", "on", "at", "to"], "answer": 1,
             "explain": "ከቀናት ስም ጋር on ይጠቀማል።"},
            {"q": "___ is your name?", "options": ["Where", "What", "When", "Why"], "answer": 1,
             "explain": "ስም ለመጠየቅ What ይጠቀማል።"},
            {"q": "He ___ go to school yesterday.", "options": ["do not", "does not", "did not", "is not"], "answer": 2,
             "explain": "ያለፈ ጊዜ አሉታዊ → did not + verb።"},
            {"q": "She is ___ than her sister.", "options": ["beautifuler", "more beautiful", "most beautiful", "beautiful"], "answer": 1,
             "explain": "ረጅም ቃል ከ more ጋር ይነጻጸራል።"},
        ],
    },
    # ───────────────────────── 7ኛ - 8ኛ ክፍል ─────────────────────────
    "eng_7_8": {
        "title": "🇬🇧 English · 7ኛ-8ኛ ክፍል",
        "lessons": [
            {
                "title": "Present Perfect",
                "body": (
                    "<b>ቅርጽ፦</b> have / has + past participle (V3)\n\n"
                    "<b>አጠቃቀም፦</b>\n"
                    "• ልምድ፦ I have visited Bahir Dar.\n"
                    "• አሁን የሚታይ ውጤት፦ I have lost my key.\n"
                    "• ጊዜ፦ She has lived here <b>for</b> 5 years / <b>since</b> 2020.\n\n"
                    "<b>ምልክቶች፦</b> just, already, yet, ever, never, for, since"
                ),
            },
            {
                "title": "Past Continuous እና Past Simple",
                "body": (
                    "<b>Past Continuous፦</b> was / were + verb-ing\n"
                    "ያለፈ ጊዜ ላይ ሲካሄድ የነበረ ድርጊት።\n\n"
                    "<b>ምሳሌ፦</b>\nI <b>was reading</b> when he <b>came</b>.\n"
                    "(ረጅም ድርጊት = was reading፣ አጭር የገባ ድርጊት = came)\n\n"
                    "<b>while</b> + continuous · <b>when</b> + simple"
                ),
            },
            {
                "title": "Modal Verbs",
                "body": (
                    "ከ modal በኋላ ሁልጊዜ verb መሠረታዊ ቅርጽ (base form) ይመጣል።\n\n"
                    "• <b>can</b> — ችሎታ፦ I can swim.\n"
                    "• <b>may / might</b> — ዕድል፦ It may rain.\n"
                    "• <b>must</b> — ግዴታ፦ You must study.\n"
                    "• <b>must not</b> — ክልክል፦ You must not smoke here.\n"
                    "• <b>should</b> — ምክር፦ You should see a doctor.\n"
                    "• <b>have to</b> — ውጫዊ ግዴታ፦ I have to wear a uniform."
                ),
            },
            {
                "title": "Quantifiers (much, many, some, any)",
                "body": (
                    "<b>many</b> + ሊቆጠር የሚችል (countable)፦ many books\n"
                    "<b>much</b> + የማይቆጠር (uncountable)፦ much water\n"
                    "<b>a lot of</b> — ለሁለቱም\n\n"
                    "<b>some</b> — አዎንታዊ፦ I have some friends.\n"
                    "<b>any</b> — አሉታዊ እና ጥያቄ፦ I don't have any money.\n\n"
                    "<b>a few</b> + countable · <b>a little</b> + uncountable"
                ),
            },
            {
                "title": "Conditionals 0 እና 1",
                "body": (
                    "<b>Zero conditional</b> — እውነታ፦\nIf + present, present\nIf you heat ice, it melts.\n\n"
                    "<b>First conditional</b> — ሊሆን የሚችል፦\nIf + present simple, will + verb\nIf it rains, we will stay at home.\n\n"
                    "<b>unless</b> = if not፦ Unless you study, you will fail."
                ),
            },
            {
                "title": "Passive Voice (መግቢያ)",
                "body": (
                    "<b>ቅርጽ፦</b> be + past participle (V3)\n\n"
                    "Active፦ The teacher <b>wrote</b> the letter.\n"
                    "Passive፦ The letter <b>was written</b> by the teacher.\n\n"
                    "<b>Present passive፦</b> is / are + V3\nEnglish is spoken here.\n\n"
                    "<b>Past passive፦</b> was / were + V3\nThe window was broken."
                ),
            },
        ],
        "quiz": [
            {"q": "I ___ already finished my homework.", "options": ["has", "have", "am", "was"], "answer": 1,
             "explain": "ከ I ጋር have + V3 (Present Perfect)።"},
            {"q": "She ___ here since 2019.", "options": ["lives", "is living", "has lived", "lived"], "answer": 2,
             "explain": "since + ነጥብ ጊዜ → Present Perfect።"},
            {"q": "I ___ TV when the phone rang.", "options": ["watched", "was watching", "watch", "have watched"], "answer": 1,
             "explain": "ረጅም ድርጊት ሲቋረጥ → Past Continuous።"},
            {"q": "You ___ park here. It is forbidden.", "options": ["must", "should", "must not", "can"], "answer": 2,
             "explain": "must not = ክልክል።"},
            {"q": "How ___ water do you need?", "options": ["many", "much", "few", "a few"], "answer": 1,
             "explain": "ውሃ uncountable ስለሆነ much።"},
            {"q": "There are ___ books on the table.", "options": ["a little", "a few", "much", "any"], "answer": 1,
             "explain": "books countable ስለሆነ a few።"},
            {"q": "If you heat water to 100 degrees, it ___.", "options": ["will boil", "boils", "boiled", "boiling"], "answer": 1,
             "explain": "እውነታ → Zero conditional (present + present)።"},
            {"q": "If it rains tomorrow, we ___ stay at home.", "options": ["will", "would", "did", "are"], "answer": 0,
             "explain": "First conditional → will + verb።"},
            {"q": "The letter ___ by the teacher.", "options": ["wrote", "was written", "is writing", "has write"], "answer": 1,
             "explain": "Past passive → was/were + V3።"},
            {"q": "You look ill. You ___ see a doctor.", "options": ["should", "can", "may not", "did"], "answer": 0,
             "explain": "ምክር ለመስጠት should ይጠቀማል።"},
        ],
    },
    # ───────────────────────── 9ኛ - 10ኛ ክፍል ─────────────────────────
    "eng_9_10": {
        "title": "🇬🇧 English · 9ኛ-10ኛ ክፍል",
        "lessons": [
            {
                "title": "ሁሉም 12 Tenses",
                "body": (
                    "<b>Present</b>\n• Simple — I work\n• Continuous — I am working\n• Perfect — I have worked\n• Perfect Continuous — I have been working\n\n"
                    "<b>Past</b>\n• Simple — I worked\n• Continuous — I was working\n• Perfect — I had worked\n• Perfect Continuous — I had been working\n\n"
                    "<b>Future</b>\n• Simple — I will work\n• Continuous — I will be working\n• Perfect — I will have worked\n• Perfect Continuous — I will have been working"
                ),
            },
            {
                "title": "Present Perfect እና Past Simple",
                "body": (
                    "<b>Past Simple</b> — የተጠናቀቀ ጊዜ ሲጠቀስ፦\nI saw him <b>yesterday</b>. · She left <b>in 2020</b>.\n\n"
                    "<b>Present Perfect</b> — ጊዜ ሳይጠቀስ ወይም ከአሁን ጋር ሲያያዝ፦\nI have seen him. · I have lost my key (አሁን የለኝም)።\n\n"
                    "💡 yesterday, last week, ago → Past Simple\nfor, since, just, already, yet → Present Perfect"
                ),
            },
            {
                "title": "Conditionals (0, 1, 2, 3)",
                "body": (
                    "<b>0</b> — If + present, present (እውነታ)\n"
                    "<b>1</b> — If + present, will + verb (ሊሆን የሚችል)\n"
                    "<b>2</b> — If + past simple, would + verb (የማይመስል / ምናባዊ)\n"
                    "If I had money, I would buy a car.\n"
                    "(በ if ዓረፍተ ነገር ውስጥ I/he/she ከ were ጋር ይሄዳል፦ If I were you...)\n\n"
                    "<b>3</b> — If + past perfect, would have + V3 (ያለፈ ፀፀት)\n"
                    "If I had studied, I would have passed."
                ),
            },
            {
                "title": "Passive Voice (በሁሉም ጊዜ)",
                "body": (
                    "<b>ቅርጽ፦</b> be (በ tense መሠረት) + V3\n\n"
                    "• Present simple — is / are + V3\n• Past simple — was / were + V3\n"
                    "• Present perfect — has / have been + V3\n• Future — will be + V3\n"
                    "• Modal — can / must be + V3\n\n"
                    "<b>ምሳሌ፦</b> The homework has been finished.\n\n"
                    "💡 የሚቀየሩት transitive verbs (ነገር የሚቀበሉ) ብቻ ናቸው።"
                ),
            },
            {
                "title": "Reported Speech",
                "body": (
                    "Direct፦ \"I am tired,\" she said.\nReported፦ She said (that) she <b>was</b> tired.\n\n"
                    "<b>ወደ ኋላ መመለስ (Backshift)፦</b>\n"
                    "present → past · will → would · can → could\n"
                    "now → then · today → that day · tomorrow → the next day\n\n"
                    "<b>ጥያቄ፦</b> He asked me where I lived. (የቃላት ቅደም ተከተል ተራ ዓረፍተ ነገር ይሆናል)"
                ),
            },
            {
                "title": "Relative Clauses",
                "body": (
                    "• <b>who</b> — ሰው፦ The man who lives next door is a doctor.\n"
                    "• <b>which</b> — ነገር፦ The book which I bought is good.\n"
                    "• <b>that</b> — ሰው ወይም ነገር\n"
                    "• <b>whose</b> — ባለቤትነት፦ The girl whose bag is red is my sister.\n"
                    "• <b>where</b> — ቦታ፦ This is the school where I studied.\n\n"
                    "<b>Non-defining</b> clause በ comma ይከበባል፦ My mother, who is a nurse, works hard."
                ),
            },
            {
                "title": "Gerund እና Infinitive",
                "body": (
                    "<b>verb + -ing</b>፦ enjoy, avoid, finish, mind, keep, suggest\nI enjoy <b>reading</b>.\n\n"
                    "<b>verb + to + verb</b>፦ want, decide, hope, plan, promise, refuse\nShe decided <b>to study</b> abroad.\n\n"
                    "<b>ትርጉም ይቀየራል፦</b>\nstop doing = ድርጊቱን ማቆም (He stopped smoking.)\nstop to do = ለሌላ ድርጊት ማቆም (He stopped to smoke.)"
                ),
            },
            {
                "title": "Phrasal Verbs እና Subject-Verb Agreement",
                "body": (
                    "<b>Phrasal verbs፦</b>\nlook for = መፈለግ · look after = መንከባከብ\ngive up = መተው · put off = ማዘግየት\ncarry on = መቀጠል · find out = ማወቅ\nrun out of = ማለቅ · turn on / off = ማብራት / ማጥፋት\n\n"
                    "<b>Subject-Verb Agreement፦</b>\n• Each / Every / Everyone → singular verb: Each of the students <b>has</b> a book.\n"
                    "• Neither of the boys <b>is</b> here.\n• News, mathematics → singular: The news <b>is</b> good.\n• Police, people → plural: The police <b>are</b> here."
                ),
            },
        ],
        "quiz": [
            {"q": "\"I have been waiting for two hours.\" — ይህ የትኛው tense ነው?",
             "options": ["Present Perfect", "Present Perfect Continuous", "Past Continuous", "Present Continuous"], "answer": 1,
             "explain": "have/has been + verb-ing = Present Perfect Continuous።"},
            {"q": "I ___ him yesterday.", "options": ["have seen", "saw", "see", "had seen"], "answer": 1,
             "explain": "yesterday ካለ Past Simple።"},
            {"q": "If I ___ rich, I would help the poor.", "options": ["am", "were", "will be", "would be"], "answer": 1,
             "explain": "Second conditional → if + past (were)።"},
            {"q": "If she had studied, she ___ the exam.", "options": ["would pass", "will pass", "would have passed", "passed"], "answer": 2,
             "explain": "Third conditional → would have + V3።"},
            {"q": "The window ___ by the boy yesterday.", "options": ["broke", "was broken", "is broken", "has broken"], "answer": 1,
             "explain": "Past passive → was + V3።"},
            {"q": "He said, \"I am tired.\" → He said he ___ tired.", "options": ["is", "was", "will be", "has been"], "answer": 1,
             "explain": "Backshift፦ am → was።"},
            {"q": "The woman ___ lives next door is a nurse.", "options": ["which", "who", "whose", "where"], "answer": 1,
             "explain": "ለሰው who ይጠቀማል።"},
            {"q": "I enjoy ___ football.", "options": ["to play", "play", "playing", "played"], "answer": 2,
             "explain": "enjoy + verb-ing።"},
            {"q": "She decided ___ abroad.", "options": ["studying", "to study", "study", "studied"], "answer": 1,
             "explain": "decide + to + verb።"},
            {"q": "«look after» ማለት ምን ማለት ነው?", "options": ["መፈለግ", "መንከባከብ", "መተው", "ማዘግየት"], "answer": 1,
             "explain": "look after = መንከባከብ፤ look for = መፈለግ።"},
            {"q": "Each of the students ___ a book.", "options": ["have", "has", "are having", "were"], "answer": 1,
             "explain": "Each → singular verb።"},
            {"q": "By next year, I ___ my degree.", "options": ["will finish", "will have finished", "finished", "am finishing"], "answer": 1,
             "explain": "By + ወደፊት ጊዜ → Future Perfect።"},
        ],
    },
    # ───────────────────────── 11ኛ - 12ኛ ክፍል ─────────────────────────
    "eng_11_12": {
        "title": "🇬🇧 English · 11ኛ-12ኛ ክፍል",
        "lessons": [
            {
                "title": "Perfect Continuous Tenses",
                "body": (
                    "<b>Present PC፦</b> have / has been + V-ing\nI have been studying for three hours.\n\n"
                    "<b>Past PC፦</b> had been + V-ing\nShe was tired because she had been working all day.\n\n"
                    "<b>Future PC፦</b> will have been + V-ing\nBy June, I will have been working here for five years.\n\n"
                    "💡 ትኩረቱ የድርጊቱ <b>ቆይታ</b> ላይ ነው።"
                ),
            },
            {
                "title": "Third እና Mixed Conditionals",
                "body": (
                    "<b>3rd፦</b> If + had + V3, would have + V3\nIf I had left earlier, I would have caught the bus.\n\n"
                    "<b>Mixed (ያለፈ → አሁን)፦</b>\nIf I had studied medicine, I would be a doctor now.\n\n"
                    "<b>ሌሎች ቃላት፦</b>\nunless = if not\nprovided that / as long as = በዚህ ሁኔታ ብቻ\nin case = ለሚመጣ አደጋ ጥንቃቄ"
                ),
            },
            {
                "title": "Wish እና If only",
                "body": (
                    "<b>wish + past simple</b> — አሁን ያለ ምኞት፦\nI wish I <b>were</b> taller.\n\n"
                    "<b>wish + past perfect</b> — የሰራነው ፀፀት፦\nI wish I <b>had studied</b> harder.\n\n"
                    "<b>wish + would</b> — ቅሬታ፦\nI wish he <b>would stop</b> shouting.\n\n"
                    "<b>If only</b> = ከ wish የበለጠ ጠንካራ፦ If only I had more time!"
                ),
            },
            {
                "title": "Causative እና Advanced Passive",
                "body": (
                    "<b>have / get + something + V3</b> (ሌላ ሰው እንዲያደርግልን)፦\nI <b>had my car repaired</b>.\nShe <b>got her hair cut</b>.\n\n"
                    "<b>It is said / believed that...</b>፦\nIt is said that he is rich.\nHe is said to be rich.\n\n"
                    "<b>ሁለት object ያለው፦</b>\nShe gave me a gift. → I was given a gift."
                ),
            },
            {
                "title": "Reported Speech (ከፍተኛ)",
                "body": (
                    "<b>Reporting verbs፦</b>\n• advise + object + to: He advised me to rest.\n• warn + object + (not) to: She warned us not to go.\n"
                    "• promise + to: He promised to come.\n• admit / deny / suggest + -ing: He denied stealing the money. She suggested going to the park.\n"
                    "• insist on + -ing · accuse sb of + -ing\n\n"
                    "💡 ከ reporting verb በኋላ የሚመጣው ቅርጽ በ verb ይወሰናል፤ ሁልጊዜ that አይደለም።"
                ),
            },
            {
                "title": "Participle Clauses እና Inversion",
                "body": (
                    "<b>Participle clauses፦</b>\nHaving finished the work, he went home.\nWalking down the street, I met an old friend.\n\n"
                    "<b>Inversion (አጽንዖት)፦</b>\nNever have I seen such a beautiful place.\nHardly had he arrived when it started to rain.\nNot only did she sing, but she also danced.\n\n"
                    "💡 አሉታዊ adverb ከዓረፍተ ነገር መጀመሪያ ሲመጣ auxiliary verb ከ subject በፊት ይመጣል።"
                ),
            },
            {
                "title": "Linking Words እና Essay Writing",
                "body": (
                    "<b>መደመር፦</b> moreover, furthermore, in addition\n<b>ተቃራኒ፦</b> however, although, despite, whereas\n"
                    "<b>ምክንያት፦</b> because of, owing to, since\n<b>ውጤት፦</b> therefore, consequently, as a result\n\n"
                    "<b>Essay መዋቅር፦</b>\n1. Introduction — ርዕስ እና thesis\n2. Body paragraphs — topic sentence + ማስረጃ + ምሳሌ\n3. Conclusion — ማጠቃለያ (አዲስ ሃሳብ አይጨመርም)"
                ),
            },
            {
                "title": "Word Formation እና Question Tags",
                "body": (
                    "<b>Prefixes፦</b> un- (unhappy) · dis- (disagree) · im- (impossible) · re- (rewrite)\n"
                    "<b>Suffixes፦</b> -tion (education) · -ment (agreement) · -ness (happiness) · -able (readable)\n\n"
                    "<b>Question tags፦</b>\nShe is a teacher, <b>isn't she?</b>\nThey don't like tea, <b>do they?</b>\nLet's go, <b>shall we?</b>\n\n"
                    "💡 አዎንታዊ ዓረፍተ ነገር → አሉታዊ tag፤ አሉታዊ → አዎንታዊ tag።"
                ),
            },
        ],
        "quiz": [
            {"q": "By June, I ___ here for five years.",
             "options": ["will work", "will have been working", "have worked", "am working"], "answer": 1,
             "explain": "By + ጊዜ እና ቆይታ → Future Perfect Continuous።"},
            {"q": "If I ___ harder, I would have passed.", "options": ["studied", "study", "had studied", "would study"], "answer": 2,
             "explain": "Third conditional → if + had + V3።"},
            {"q": "I wish I ___ taller.", "options": ["am", "was", "were", "will be"], "answer": 2,
             "explain": "አሁን ያለ ምኞት → wish + past (were)።"},
            {"q": "I wish I ___ harder last year.", "options": ["studied", "had studied", "would study", "study"], "answer": 1,
             "explain": "ያለፈ ፀፀት → wish + past perfect።"},
            {"q": "I had my car ___ yesterday.", "options": ["repair", "repairing", "repaired", "to repair"], "answer": 2,
             "explain": "have + object + V3 (causative)።"},
            {"q": "He denied ___ the money.", "options": ["to steal", "stealing", "steal", "stole"], "answer": 1,
             "explain": "deny + verb-ing።"},
            {"q": "___ finished the work, he went home.", "options": ["Have", "Having", "Had", "To have"], "answer": 1,
             "explain": "Participle clause → Having + V3።"},
            {"q": "Never ___ such a beautiful place.", "options": ["I have seen", "have I seen", "I saw", "did I saw"], "answer": 1,
             "explain": "Never ከመጀመሪያ ሲመጣ inversion → have I seen።"},
            {"q": "«However» ምን ዓይነት linking word ነው?", "options": ["መደመር", "ተቃራኒ", "ምክንያት", "ውጤት"], "answer": 1,
             "explain": "however = ነገር ግን (contrast)።"},
            {"q": "የ «happy» ተቃራኒ በ prefix የቱ ነው?", "options": ["inhappy", "unhappy", "dishappy", "nonhappy"], "answer": 1,
             "explain": "happy → unhappy (prefix un-)።"},
            {"q": "She is a teacher, ___?", "options": ["is she", "isn't she", "doesn't she", "won't she"], "answer": 1,
             "explain": "አዎንታዊ ዓረፍተ ነገር → አሉታዊ tag።"},
            {"q": "\"Unless you hurry, you will be late.\" ማለት ምን ማለት ነው?",
             "options": ["If you hurry, you will be late.", "If you don't hurry, you will be late.",
                         "If you hurried, you would be late.", "You hurry because you are late."], "answer": 1,
             "explain": "unless = if ... not።"},
        ],
    },
}
