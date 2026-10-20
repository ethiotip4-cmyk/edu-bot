# -*- coding: utf-8 -*-
"""
የትምህርት እና የጥያቄ ይዘት።
አዲስ ትምህርት ወይም ጥያቄ ለመጨመር ከታች ያለውን ቅርጽ ገልብጠህ ጨምር።
- ትምህርት body ውስጥ <b>ደማቅ</b> ብቻ ተጠቀም። "<" ወይም "&" ምልክት አትጠቀም።
- answer = ትክክለኛው አማራጭ ቁጥር (ከ 0 ይጀምራል)።
"""

CATEGORIES = {
    "school": "🏫 የትምህርት ቤት (9-12)",
    "tech": "💻 ቴክኖሎጂ",
    "lang": "🗣 እንግሊዝኛ ቋንቋ",
}

LESSONS = {
    "school": [
        {
            "title": "የፓይታጎረስ ንድፈ ሐሳብ",
            "body": (
                "በቀኝ ማዕዘን ሦስት ማዕዘን (right triangle) ውስጥ፦\n\n"
                "<b>a² + b² = c²</b>\n\n"
                "• a እና b — ቀኝ ማዕዘንን የሚሠሩ ጎኖች\n"
                "• c — ከቀኝ ማዕዘን ተቃራኒ ያለው ረጅሙ ጎን (hypotenuse)\n\n"
                "<b>ምሳሌ፦</b> a = 3, b = 4 ቢሆን\n"
                "3² + 4² = 9 + 16 = 25\n"
                "ስለዚህ c = √25 = 5\n\n"
                "💡 የሦስት ማዕዘን ሦስቱ ውስጣዊ ማዕዘኖች ድምር ሁልጊዜ 180° ነው።"
            ),
        },
        {
            "title": "የኒውተን የእንቅስቃሴ ህጎች",
            "body": (
                "<b>1ኛ ህግ (ኢነርሺያ)፦</b> ውጫዊ ኃይል ካልተሠራበት ነገር ባለበት ይቆያል፣ "
                "ወይም በቀጥታ መስመር በቋሚ ፍጥነት ይንቀሳቀሳል።\n\n"
                "<b>2ኛ ህግ፦</b> F = m × a\n"
                "ኃይል (N) = ጅምላ (kg) × ፍጥነት መጨመር (m/s²)\n"
                "ምሳሌ፦ 10 kg ነገር በ 2 m/s² ቢፈጥን → F = 20 N\n\n"
                "<b>3ኛ ህግ፦</b> ለእያንዳንዱ ድርጊት እኩል እና ተቃራኒ ምላሽ አለ።\n"
                "ምሳሌ፦ ሮኬት ጋዝን ወደ ታች ሲገፋ ጋዙ ሮኬቱን ወደ ላይ ይገፋዋል።"
            ),
        },
        {
            "title": "ሕዋስ እና ፎቶሲንተሲስ",
            "body": (
                "<b>ሕዋስ (Cell)</b> የሕይወት መሠረታዊ አሃድ ነው።\n\n"
                "• <b>ኒውክሊየስ</b> — የሕዋስ መቆጣጠሪያ፤ ዘረ-መል (DNA) ይይዛል\n"
                "• <b>ሚቶኮንድሪያ</b> — የሕዋስ የኃይል ማመንጫ\n"
                "• <b>ክሎሮፕላስት</b> — በተክል ሕዋስ ውስጥ ብቻ፤ ፎቶሲንተሲስ የሚካሄድበት\n\n"
                "<b>ፎቶሲንተሲስ፦</b> ተክሎች የፀሐይ ብርሃንን ተጠቅመው ከካርቦን ዳይኦክሳይድ (CO₂) "
                "እና ከውሃ (H₂O) ምግብ (ግሉኮስ) እና ኦክስጅን ይሠራሉ።"
            ),
        },
    ],
    "tech": [
        {
            "title": "ኮምፒውተር እንዴት ይሠራል?",
            "body": (
                "• <b>CPU</b> (Central Processing Unit) — የኮምፒውተር «አንጎል»፤ ትዕዛዞችን ያከናውናል\n"
                "• <b>RAM</b> — ጊዜያዊ ማህደረ ትውስታ፤ ኮምፒውተሩ ሲጠፋ ይጸዳል\n"
                "• <b>Storage (SSD/HDD)</b> — ፋይሎችን ለዘለቄታው ያስቀምጣል\n"
                "• <b>OS</b> — ሃርድዌሩን የሚያስተዳድር ሶፍትዌር (Windows, Android, ...)\n\n"
                "<b>መለኪያዎች፦</b>\n"
                "1 byte = 8 bits\n"
                "1 KB ≈ 1,000 bytes\n"
                "1 MB ≈ 1,000 KB"
            ),
        },
        {
            "title": "የኢንተርኔት ደህንነት",
            "body": (
                "• <b>ጠንካራ password፦</b> ቢያንስ 12 ፊደላት፣ ትልልቅና ትናንሽ ፊደላት፣ ቁጥሮች እና ምልክቶች ቅልቅል። "
                "ስምህን ወይም የልደት ቀንህን አትጠቀም።\n\n"
                "• <b>2FA (ባለ ሁለት ደረጃ ማረጋገጫ)</b> — password ቢሰረቅ እንኳ መለያህን ይጠብቃል።\n\n"
                "• <b>Phishing</b> — አጭበርባሪዎች ሐሰተኛ መልእክት ወይም ድረ-ገጽ ተጠቅመው መረጃህን የሚሰርቁበት ዘዴ። "
                "አጠራጣሪ link በጭራሽ አትክፈት።\n\n"
                "• <b>HTTPS</b> — በአድራሻው ውስጥ ያለው «S» ማለት Secure፤ ግንኙነቱ የተመሰጠረ ነው።"
            ),
        },
        {
            "title": "ሰው ሰራሽ ብልህነት (AI) መግቢያ",
            "body": (
                "AI ኮምፒውተሮች ከመረጃ ተምረው ብልህ የሚመስሉ ሥራዎችን እንዲያከናውኑ የሚያደርግ ቴክኖሎጂ ነው።\n\n"
                "• <b>Machine Learning</b> — ኮምፒውተር ከብዙ ምሳሌዎች ንድፍ ይማራል\n"
                "• <b>Chatbot</b> — እንደ ሰው የሚያወራ ፕሮግራም (ይህ bot ጭምር!)\n"
                "• <b>Prompt</b> — ለ AI የምትሰጠው መመሪያ ወይም ጥያቄ\n\n"
                "💡 ጥሩ prompt ግልጽ፣ ዝርዝር እና ምሳሌ ያለው ነው። AI ሊሳሳት ስለሚችል "
                "አስፈላጊ መረጃዎችን ሁልጊዜ አረጋግጥ።"
            ),
        },
    ],
    "lang": [
        {
            "title": "ሰላምታ (Greetings)",
            "body": (
                "• <b>Hello / Hi</b> — ሰላም\n"
                "• <b>Good morning</b> — እንደምን አደርክ/ሽ (ጠዋት)\n"
                "• <b>Good afternoon</b> — እንደምን ዋልክ/ሽ\n"
                "• <b>Good evening</b> — እንደምን አመሸህ/ሽ\n"
                "• <b>How are you?</b> — እንዴት ነህ/ነሽ?\n"
                "• <b>I'm fine, thank you.</b> — ደህና ነኝ፣ አመሰግናለሁ።\n"
                "• <b>Thank you</b> → <b>You're welcome</b> — አመሰግናለሁ → ምንም አይደል\n"
                "• <b>Nice to meet you</b> — ስላገኘሁህ/ሽ ደስ ብሎኛል"
            ),
        },
        {
            "title": "To be (am / is / are)",
            "body": (
                "I → <b>am</b>: I am a student.\n"
                "He / She / It → <b>is</b>: She is a teacher.\n"
                "You / We / They → <b>are</b>: They are friends.\n\n"
                "<b>አሉታዊ፦</b> I am not · He is not · They are not\n"
                "<b>ጥያቄ፦</b> Are you ready? · Is she at home?"
            ),
        },
        {
            "title": "Present Simple (የዘወትር ድርጊት)",
            "body": (
                "ዘወትር የሚደረግ ድርጊትን ለመግለጽ ይጠቅማል፦\n\n"
                "I / You / We / They + verb → I <b>play</b> football.\n"
                "He / She / It + verb<b>+s</b> → She <b>goes</b> to school.\n\n"
                "<b>አሉታዊ፦</b> do not / does not + verb\n"
                "He does not like tea.\n\n"
                "<b>ጥያቄ፦</b> Do you study? · Does she work?\n\n"
                "💡 <b>ተጨማሪ — ያለፈ ጊዜ ልዩ ግሦች፦</b>\n"
                "go → went · eat → ate · see → saw"
            ),
        },
    ],
}

QUIZ = {
    "school": [
        {
            "q": "የሦስት ማዕዘን ሦስቱ ውስጣዊ ማዕዘኖች ድምር ስንት ነው?",
            "options": ["90°", "180°", "270°", "360°"],
            "answer": 1,
            "explain": "የማንኛውም ሦስት ማዕዘን ውስጣዊ ማዕዘኖች ድምር 180° ነው።",
        },
        {
            "q": "በቀኝ ማዕዘን ሦስት ማዕዘን ሁለቱ ጎኖች 3 እና 4 ቢሆኑ፣ ረጅሙ ጎን (hypotenuse) ስንት ነው?",
            "options": ["5", "6", "7", "12"],
            "answer": 0,
            "explain": "3² + 4² = 9 + 16 = 25፣ √25 = 5።",
        },
        {
            "q": "የኒውተን 1ኛ ህግ ስለ ምን ይናገራል?",
            "options": [
                "ኢነርሺያ (ባለበት የመቆየት ባሕርይ)",
                "ድርጊት እና ምላሽ",
                "የስበት ኃይል ብቻ",
                "የብርሃን ፍጥነት",
            ],
            "answer": 0,
            "explain": "ውጫዊ ኃይል ካልተሠራበት ነገር ባለበት ይቆያል ወይም በቋሚ ፍጥነት ይንቀሳቀሳል።",
        },
        {
            "q": "5 kg ጅምላ ያለው ነገር በ 4 m/s² ቢፈጥን፣ የሚሠራበት ኃይል ስንት ነው?",
            "options": ["9 N", "20 N", "1.25 N", "54 N"],
            "answer": 1,
            "explain": "F = m × a = 5 × 4 = 20 N።",
        },
        {
            "q": "«የሕዋስ የኃይል ማመንጫ» የሚባለው የትኛው ክፍል ነው?",
            "options": ["ኒውክሊየስ", "ሚቶኮንድሪያ", "ክሎሮፕላስት", "ሪቦዞም"],
            "answer": 1,
            "explain": "ሚቶኮንድሪያ ለሕዋሱ የሚያስፈልገውን ኃይል ያመነጫል።",
        },
        {
            "q": "ተክሎች ለፎቶሲንተሲስ ከአየር የሚወስዱት ጋዝ የትኛው ነው?",
            "options": ["ኦክስጅን", "ናይትሮጅን", "ካርቦን ዳይኦክሳይድ", "ሃይድሮጅን"],
            "answer": 2,
            "explain": "ተክሎች CO₂ ወስደው ኦክስጅን ይለቃሉ።",
        },
        {
            "q": "የውሃ ኬሚካላዊ ቀመር የቱ ነው?",
            "options": ["CO₂", "H₂O", "O₂", "NaCl"],
            "answer": 1,
            "explain": "ውሃ ሁለት ሃይድሮጅን እና አንድ ኦክስጅን አቶም አለው — H₂O።",
        },
        {
            "q": "ሮኬት ወደ ላይ የሚወጣው በየትኛው የኒውተን ህግ ነው?",
            "options": ["1ኛ ህግ", "2ኛ ህግ", "3ኛ ህግ", "የትኛውም አይደለም"],
            "answer": 2,
            "explain": "ሮኬት ጋዝን ወደ ታች ሲገፋ ጋዙ ሮኬቱን ወደ ላይ ይገፋዋል፤ ይህ የድርጊት-ምላሽ ህግ ነው።",
        },
    ],
    "tech": [
        {
            "q": "CPU ምን ማለት ነው?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Core Power Unit",
            ],
            "answer": 0,
            "explain": "CPU የኮምፒውተር ትዕዛዞችን የሚያከናውን ዋና ክፍል ነው።",
        },
        {
            "q": "ከሚከተሉት ውስጥ ጠንካራው password የትኛው ነው?",
            "options": ["123456", "dagim2000", "Kp#8vL!x2Qr9", "password"],
            "answer": 2,
            "explain": "ረጅም ሲሆን ፊደል፣ ቁጥር እና ምልክት ቅልቅል አለው፤ ሊገመት አይችልም።",
        },
        {
            "q": "በ HTTPS ውስጥ ያለው «S» ምን ማለት ነው?",
            "options": ["Simple", "Secure", "Server", "Speed"],
            "answer": 1,
            "explain": "HTTPS = HyperText Transfer Protocol Secure፤ ግንኙነቱ የተመሰጠረ ነው።",
        },
        {
            "q": "RAM ምን ያደርጋል?",
            "options": [
                "ፋይሎችን ለዘለቄታው ያስቀምጣል",
                "ጊዜያዊ ማህደረ ትውስታ ነው",
                "ስክሪን ያሳያል",
                "ኢንተርኔት ያገናኛል",
            ],
            "answer": 1,
            "explain": "RAM ኮምፒውተሩ እየሠራ ያለውን መረጃ ለጊዜው ይይዛል፤ ሲጠፋ ይጸዳል።",
        },
        {
            "q": "Phishing ምንድን ነው?",
            "options": [
                "ኮምፒውተር ማጽዳት",
                "ተጠቃሚን በማታለል መረጃ መስረቅ",
                "ፈጣን ኢንተርኔት",
                "ፋይል መጭመቅ",
            ],
            "answer": 1,
            "explain": "አጭበርባሪዎች ሐሰተኛ መልእክት ወይም ድረ-ገጽ ተጠቅመው መረጃ ይሰርቃሉ።",
        },
        {
            "q": "1 byte ስንት bits ነው?",
            "options": ["4 bits", "8 bits", "16 bits", "10 bits"],
            "answer": 1,
            "explain": "1 byte = 8 bits።",
        },
        {
            "q": "2FA (ባለ ሁለት ደረጃ ማረጋገጫ) ጥቅሙ ምንድን ነው?",
            "options": [
                "ኢንተርኔት ማፍጠን",
                "password ቢሰረቅ መለያን መጠበቅ",
                "ፋይል መሰረዝ",
                "ባትሪ መቆጠብ",
            ],
            "answer": 1,
            "explain": "ከ password በተጨማሪ ሁለተኛ ማረጋገጫ ስለሚጠየቅ መለያህ ይጠበቃል።",
        },
        {
            "q": "ለ AI የምትሰጠው መመሪያ ወይም ጥያቄ ምን ይባላል?",
            "options": ["Battery", "Prompt", "Virus", "Router"],
            "answer": 1,
            "explain": "Prompt ግልጽ እና ዝርዝር ሲሆን AI የተሻለ መልስ ይሰጣል።",
        },
    ],
    "lang": [
        {
            "q": "I ___ a student.",
            "options": ["am", "is", "are", "be"],
            "answer": 0,
            "explain": "ከ I ጋር am ይሄዳል።",
        },
        {
            "q": "She ___ to school every day.",
            "options": ["go", "goes", "going", "gone"],
            "answer": 1,
            "explain": "ከ He/She/It ጋር በ Present Simple ግሱ ላይ s/es ይጨመራል።",
        },
        {
            "q": "They ___ playing football.",
            "options": ["is", "am", "are", "be"],
            "answer": 2,
            "explain": "ከ They ጋር are ይሄዳል።",
        },
        {
            "q": "«Good morning» ማለት ምን ማለት ነው?",
            "options": [
                "እንደምን ዋልክ",
                "እንደምን አደርክ (ጠዋት)",
                "ደህና ሁን",
                "አመሰግናለሁ",
            ],
            "answer": 1,
            "explain": "Good morning በጠዋት የሚባል ሰላምታ ነው።",
        },
        {
            "q": "አንድ ሰው «Thank you» ሲልህ የሚመጥነው መልስ የቱ ነው?",
            "options": ["You're welcome", "Good night", "I am sorry", "See you"],
            "answer": 0,
            "explain": "«You're welcome» ማለት «ምንም አይደል» ማለት ነው።",
        },
        {
            "q": "He ___ not like tea.",
            "options": ["do", "does", "is", "are"],
            "answer": 1,
            "explain": "ከ He/She/It ጋር በአሉታዊ ዓረፍተ ነገር does not ይጠቀማል።",
        },
        {
            "q": "የ «go» ያለፈ ጊዜ ቅርጽ የቱ ነው?",
            "options": ["goed", "went", "gone", "going"],
            "answer": 1,
            "explain": "go → went (ልዩ ግስ)።",
        },
        {
            "q": "የ «child» ብዙ ቁጥር የቱ ነው?",
            "options": ["childs", "childes", "children", "childrens"],
            "answer": 2,
            "explain": "child → children (ልዩ ብዙ ቁጥር)።",
        },
    ],
}
