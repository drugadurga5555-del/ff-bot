import telebot, requests, os
from flask import Flask
import threading

TOKEN = "8994456344:AAH5TsZg6bkcDJvdU3F3q6B2TctFQzfghho"
bot = telebot.TeleBot(TOKEN)
bot.delete_webhook(drop_pending_updates=True)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Alive - 409 Fixed"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask, daemon=True).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "✅ Bot ON hai! Ab bhejo:\n/info 3513765300")

@bot.message_handler(func=lambda m: True)
def handle(m):
    txt = m.text.replace("/info","").replace("/start","").strip()
    if not txt.isdigit():
        return
    uid = txt
    try:
        url = f"https://freefire-api-six.vercel.app/get_player_personal_show?server=ind&uid={uid}"
        r = requests.get(url, timeout=15)
        if len(r.text) > 10:
            bot.reply_to(m, f"Result for {uid}:\n{r.text[:3500]}")
        else:
            bot.reply_to(m, f"UID {uid} ka data nahi mila. Region IND try kiya.")
    except Exception as e:
        bot.reply_to(m, f"Error: {e}")

print("Bot Starting...")
bot.infinity_polling(skip_pending=True)
