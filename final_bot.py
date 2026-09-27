import telebot, requests, os
from flask import Flask
import threading

TOKEN = "8994456344:AAFeBNAD_9GvZ8Osa54Dfp-QYeDWYtktiUM" # apna token yahi rahega

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
@app.route('/')
def home(): return "Bot Alive"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot ON hai ✅\n/info 3513765300 bhejo")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    text = m.text.strip()
    uid = text.replace("/info","").replace("/like","").strip()
    if not uid.isdigit():
        bot.reply_to(m, "UID bhejo: /info 3513765300")
        return
    try:
        bot.send_message(m.chat.id, f"⏳ {uid} ka info...")
        # Public Info API
        url = f"https://api.freefireinfo.site/info?uid={uid}&region=ind"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            bot.send_message(m.chat.id, f"✅ Info:\n\n{r.text[:2000]}")
        else:
            bot.send_message(m.chat.id, f"API Down hai ({r.status_code}), 5 min baad try kar")
    except Exception as e:
        bot.send_message(m.chat.id, f"Error: {e}")

print("Bot Starting...")
bot.infinity_polling()
