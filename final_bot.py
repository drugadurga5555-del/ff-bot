import telebot, requests, os
from flask import Flask
import threading

TOKEN = "8994456344:AAH5TsZg6bkcDJvdU3F3q6B2TctFQzfghho"
bot = telebot.TeleBot(TOKEN)
bot.delete_webhook(drop_pending_updates=True)

app = Flask(__name__)
@app.route('/')
def home(): return "Bot Alive"
threading.Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000))), daemon=True).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot ON ✅ Ab /info UID bhejo\nEx: /info 3513765300")

@bot.message_handler(func=lambda m: True)
def handle(m):
    uid = m.text.replace("/info","").strip()
    if not uid.isdigit(): return
    try:
        url = f"https://freefire-api-six.vercel.app/get_player_personal_show?server=ind&uid={uid}"
        r = requests.get(url, timeout=15).json()
        # Iska response JSON me aata hai
        if "AccountInfo" in str(r):
            bot.reply_to(m, f"✅ Found:\n{str(r)[:3000]}")
        else:
            bot.reply_to(m, f"Result:\n{str(r)[:3000]}")
    except Exception as e:
        bot.reply_to(m, f"API Error: {e}")

print("Bot Starting...")
bot.infinity_polling(skip_pending=True)
