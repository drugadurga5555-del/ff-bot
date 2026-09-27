import telebot, requests
BOT_TOKEN = "8994456344:AAF-CPxn9nZNmjRv92BrP1h8lsw3uGV_OJI"
bot = telebot.TeleBot(BOT_TOKEN)

API = "https://level-info-ob55-seven.vercel.app/level?uid={uid}&region={region}"

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, """🔥 Level Info OB55 Bot Ready!

Use karo:
`3513765300 IND` - IND region
`3513765300 BR` - Brazil
`3513765300 SG` - Singapore

Ya sirf UID bhejo, auto IND lega:
`3513765300`
""", parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
def info(m):
    text = m.text.strip()
    parts = text.replace("/level","").strip().split()

    if not parts or not parts[0].isdigit():
        bot.reply_to(m, "UID bhejo jaise: 3513765300 IND")
        return

    uid = parts[0]
    region = parts[1].upper() if len(parts) > 1 else "IND"

    bot.send_message(m.chat.id, f"⏳ {uid} [{region}] ka level nikal raha hu...")

    try:
        url = API.format(uid=uid, region=region)
        r = requests.get(url, timeout=15)
        data = r.json()

        msg = f"""
🎮 **OB55 Level Info**

🆔 UID: {uid}
🌍 Region: {region}
👤 Name: {data.get('name', data.get('nickname','N/A'))}
⭐ Level: {data.get('level','N/A')}
❤️ Likes: {data.get('likes','N/A')}
📊 Exp: {data.get('exp','N/A')}

Full Response:

"""
        bot.send_message(m.chat.id, msg, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(m.chat.id, f"❌ Error: {e}\nAPI Response: {r.text[:1000] if 'r' in locals() else 'No response'}")

print("Level Info Bot Started... Telegram pe /start bhejo")
bot.infinity_polling()
