import telebot, requests
BOT_TOKEN = "8994456344:AAF-CPxn9nZNmjRv92BrP1h8lsw3uGV_OJI"
bot = telebot.TeleBot(BOT_TOKEN)

def send_like(uid):
    # Try 3 different public like apis
    apis = [
        f"https://like-api-taupe.vercel.app/like?uid={uid}",
        f"https://ff-like-api.vercel.app/like?uid={uid}",
        f"https://free-fire-like-api.vercel.app/like?uid={uid}&server=ind"
    ]
    results = []
    for api in apis:
        try:
            r = requests.get(api, timeout=15)
            results.append(f"{api}\n=> {r.text[:400]}")
            if "success" in r.text.lower() or "liked" in r.text.lower():
                break
        except Exception as e:
            results.append(f"{api} Error: {e}")
    return "\n\n".join(results)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 FF Like Bot V2 Ready!\n\nBas UID bhejo: 3513765300")

@bot.message_handler(func=lambda m: True)
def handle(m):
    uid = m.text.replace("/like","").strip()
    if not uid.isdigit():
        return
    bot.send_message(m.chat.id, f"⏳ {uid} pe like bhej raha hu...")
    res = send_like(uid)
    bot.send_message(m.chat.id, f"Result:\n{res[:3500]}")

print("V2 Bot Started...")
bot.infinity_polling()
