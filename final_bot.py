import telebot, requests, os
from flask import Flask
import threading

TOKEN = "8994456344:AAH5TsZg6bkcDJvdU3F3q6B2TctFQzfghho" # <-- yaha apna naya token dalna
JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." # <-- apna JWT yaha dalna agar hai to

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
@app.route('/')
def home(): return "Bot Alive"
threading.Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot ON ✅\n/info 3513765300 bhejo\nYa seedha UID bhejo")

@bot.message_handler(func=lambda m: True)
def info(m):
    txt = m.text.replace("/info","").replace("/like","").strip()
    if not txt.isdigit():
        bot.reply_to(m, "Sahi UID bhejo: /info 3513765300")
        return
    
    uid = txt
    bot.send_message(m.chat.id, f"⏳ {uid} ka info nikal raha hu...")
    
    apis = [
        f"https://free-fire-api-v1-rho.vercel.app/api/info?uid={uid}",
        f"https://ff-info-api-psi.vercel.app/info?uid={uid}",
        f"https://freefireinfo-api.vercel.app/api/player?uid={uid}&region=ind",
        f"https://api.freefireinfo.in/info?uid={uid}"
    ]
    
    for api in apis:
        try:
            r = requests.get(api, timeout=10)
            if r.status_code == 200 and "uid" in r.text.lower():
                data = r.json()
                # Accha format me bhejna
                msg = f"✅ **Player Info**\n\n"
                msg += f"UID: {uid}\n"
                msg += f"Name: {data.get('name','N/A')}\n"
                msg += f"Level: {data.get('level','N/A')}\n"
                msg += f"Likes: {data.get('likes','N/A')}\n"
                msg += f"Bio: {data.get('bio','')[:200]}\n"
                msg += f"\nFull: {str(data)[:1500]}"
                bot.send_message(m.chat.id, msg)
                return
        except:
            continue
    
    bot.send_message(m.chat.id, "❌ Saare Info API down hai. 5 min baad try karo ya JWT update karo.")

print("Bot Starting...")
bot.infinity_polling()
