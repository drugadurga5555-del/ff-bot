import telebot, requests
BOT_TOKEN = "8994456344:AAF-CPxn9nZNmjRv92BrP1h8lsw3uGV_OJI"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "✅ Info Bot Fix Ready!\n\nBhejo: 3513765300 IND\nYa: 3513765300 ind (small me)")

@bot.message_handler(func=lambda m: True)
def handle(m):
    parts = m.text.strip().split()
    if not parts[0].isdigit():
        return
    uid = parts[0]
    region = parts[1].lower() if len(parts)>1 else "ind"

    bot.send_message(m.chat.id, f"⏳ Try kar raha hu {uid} [{region}]...")

    # 3 API try karega
    urls = [
        f"https://level-info-ob55-seven.vercel.app/level?uid={uid}&region={region}",
        f"https://level-info-ob55-seven.vercel.app/level?uid={uid}&region={region.upper()}",
        f"https://level-info-ob55-seven.vercel.app/api/level?uid={uid}&region={region}"
    ]

    for url in urls:
        try:
            print(f"Trying {url}")
            r = requests.get(url, timeout=30) # 30 sec timeout
            print(f"Status {r.status_code}: {r.text[:200]}")
            bot.send_message(m.chat.id, f"✅ Success!\nURL: {url}\n\n{ r.text[:3500] }")
            return
        except Exception as e:
            print(f"Fail {url}: {e}")
            continue

    bot.send_message(m.chat.id, "❌ 3 baar try kiya, API respond nahi kar rahi.\n\nTeri API Vercel pe so gayi hai. 1 min baad fir se /start karke try kar, ya fir apni API ka code mujhe bhej mai fast bana dunga.")

print("Fix Bot Started...")
bot.infinity_polling()
