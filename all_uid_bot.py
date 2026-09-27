import telebot, requests
BOT_TOKEN = "8994456344:AAF-CPxn9nZNmjRv92BrP1h8lsw3uGV_OJI"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "✅ All UID Info Bot Ready!\n\nKoi bhi UID bhejo:\n3513765300\n123456789\n\nRegion ke saath: 3513765300 ind")

@bot.message_handler(func=lambda m: True)
def handle(m):
    text = m.text.strip().split()
    uid = text[0].replace("/level","").replace("/info","")
    if not uid.isdigit():
        bot.reply_to(m, "Sahi UID bhejo")
        return

    region = text[1] if len(text) > 1 else "ind"
    bot.send_message(m.chat.id, f"⏳ {uid} [{region}] check kar raha hu...")

    try:
        url = f"https://level-info-ob55-seven.vercel.app/level?uid={uid}&region={region}"
        r = requests.get(url, timeout=30)
        data = r.json()
        info = data.get('Level Information', data)

        if not info or 'UID' not in str(info):
            bot.send_message(m.chat.id, f"❌ UID {uid} nahi mili. Shayad galat UID hai.\n\nResponse: {r.text[:1000]}")
            return

        msg = f"""🎮 FF INFO

🆔 UID: {info.get('UID', uid)}
👤 Name: {info.get('Username','N/A')}
⭐ Level: {info.get('Level','N/A')}
❤️ Likes: {info.get('Likes','N/A')}
🔹 Exp: {info.get('Exp','N/A')}
📊 Progress: {info.get('Level Progress','N/A')}%
🌍 Region: {info.get('Region', region)}
"""
        bot.send_message(m.chat.id, msg)
    except Exception as e:
        bot.send_message(m.chat.id, f"Error: {e}")

print("All UID Bot Started - Telegram pe koi bhi UID bhejo")
bot.infinity_polling()
