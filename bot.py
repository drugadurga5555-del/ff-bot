import telebot, requests, os
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def handle(m):
    text = m.text.split()[0].replace("/","")
    if not text.isdigit(): return
    try:
        r = requests.get(f"https://level-info-ob55-seven.vercel.app/level?uid={text}&region=ind", timeout=20).json()
        info = r.get('Level Information', r)
        bot.reply_to(m, f"UID: {info.get('UID')}\nName: {info.get('Username')}\nLevel: {info.get('Level')}\nLikes: {info.get('Likes')}")
    except Exception as e:
        bot.reply_to(m, f"Error: {e}")

bot.infinity_polling()
