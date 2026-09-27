import telebot, requests, os
from flask import Flask
import threading

TOKEN = "8994456344:AAH5TsZg6bkcDJvdU3F3q6B2TctFQzfghho"  # Jo abhi revoke karke mila hai wo
bot = telebot.TeleBot(TOKEN)

# YE LINE SABSE IMPORTANT HAI - 409 FIX KAREGA
bot.delete_webhook(drop_pending_updates=True)

app = Flask(__name__)
@app.route('/')
def home(): return "Bot Alive"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask, daemon=True).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot ON ✅ Ab /info 3513765300 bhejo")

@bot.message_handler(func=lambda m: True)
def handle(m):
    txt = m.text.replace("/info","").strip()
    if not txt.isdigit(): return
    uid = txt
    try:
        r = requests.get(f"https://free-fire-api-v1-rho.vercel.app/api/info?uid={uid}", timeout=10)
        bot.reply_to(m, f"Result:\n{r.text[:3000]}")
    except Exception as e:
        bot.reply_to(m, f"Error: {e}")

print("Bot Starting...")
bot.infinity_polling(skip_pending=True)
