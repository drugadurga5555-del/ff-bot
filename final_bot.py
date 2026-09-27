import os
import threading
import requests
import telebot
from flask import Flask

TOKEN = "8994456344:AAH5TsZg6bkcDJvdU3F3q6B2TctFQzfghho"
API_KEY = "GtxRUZFiEbZkjtMDpGVCoWn0ZyMbCz_HKhCMuQTwSXI"

bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

def run_bot():
    bot.infinity_polling(skip_pending=True)

threading.Thread(target=run_bot, daemon=True).start()

@bot.message_handler(commands=['start'])
def start_cmd(m):
    bot.reply_to(m, "✅ Bot ON Hai!\nUse: /info 3513765300")

@bot.message_handler(func=lambda m: True)
def handle_all(m):
    text = m.text.strip()
    uid = text.replace("/info", "").strip()
    if not uid.isdigit():
        bot.reply_to(m, "UID bhejo: /info 3513765300")
        return
    try:
        url = f"https://api.gameskinbo.com/freefire/info?uid={uid}&region=ind"
        headers = {"X-API-Key": API_KEY, "api-key": API_KEY}
        r = requests.get(url, headers=headers, timeout=20)
        data = r.text
        if len(data) > 4000:
            data = data[:4000]
        bot.reply_to(m, f"Result for {uid}:\n{data}")
    except Exception as e:
        bot.reply_to(m, f"Error: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
