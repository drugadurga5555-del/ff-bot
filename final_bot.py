import telebot, requests, os
from flask import Flask
import threading

TOKEN = "8994456344:AAH5TsZg6bkcDJvdU3F3q6B2TctFQzfghho"
API_KEY = "GtxRUZFiEbZkjtMDpGVCoWn0ZyMbCz_HKhCMuQTwSXI"

bot = telebot.TeleBot(TOKEN)
bot.delete_webhook(drop_pending_updates=True)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Alive - Working"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask, daemon=True).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "✅ Bot ON hai!\nUse: /info 3513765300")

@bot.message_handler(func=lambda m: True)
def handle(m):
    txt = m.text.replace("/info","").replace("/start","").strip()
    if not txt.isdigit():
        return
    uid = txt
    bot.send_message(m.chat.id, f"🔍 Checking UID {uid}...")
    try:
        # Try 1: GamesKinbo API
        headers = {"X-API-Key": API_KEY, "api-key": API_KEY, "Authorization": API_KEY}
        url = f"https://api.gameskinbo.com/freefire/info?uid={uid}&region=ind"
        r = requests.get(url, headers=headers, timeout=20)
        
        if r.status_code == 200 and len(r.text) > 20 and "MAJOR_LOGIN_FAILED" not in r.text:
            data = r.text
