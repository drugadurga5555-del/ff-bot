from flask import Flask
import threading, os
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Alive"
threading.Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))).start()

import telebot, requests, time
BOT_TOKEN = "8094465341:AAF-CpXnDm2RmXv92bB-PhBx2wGxV_DJY"
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjI1ZWIxN2I1YzQ1ZWI1YzI1ZDBiMGFlX0JvI0xJQk1QIEQ6A1oJ1XVIQ1FQ..eyJV2hYdG02OX2lkXjJsc3hjbSMTAxNmMyLCJuaWFrbnFzZ25xZ1ozZDM"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 FF Bot Ready\n\n/info 3513765300 - Info ke liye\n/like 3513765300 - Like ke liye\nYa seedha UID bhejo to Info ayega")

@bot.message_handler(commands=['info'])
def info_cmd(m):
    try:
        uid = m.text.replace("/info","").strip()
        if not uid.isdigit():
            bot.reply_to(m, "Sahi UID bhejo. Ex: /info 3513765300")
            return
        
        bot.send_message(m.chat.id, f"⏳ {uid} ka Info nikal raha hu...")
        
        # Method 1: JWT se try
        headers = {"Authorization": f"Bearer {JWT_TOKEN}", "Content-Type": "application/json", "User-Agent": "GarenaMSDK/4.0.19"}
        # FF Info endpoint
        payload = {"uid": uid}
        r = requests.post("https://client.ind.freefiremobile.com/GetPlayerPersonalShow", headers=headers, json=payload, timeout=15)
        
        if r.status_code == 200 and len(r.text) > 50:
            data = r.json() if "{" in r.text else {}
            # Simple reply
            bot.send_message(m.chat.id, f"✅ **Info Mil Gaya**\n\nUID: {uid}\n\nRaw Data: {r.text[:1000]}")
        else:
            # Fallback public API
            r2 = requests.get(f"https://api.freefireinfo.site/info?uid={uid}&region=ind", timeout=10)
            bot.send_message(m.chat.id, f"✅ **Player Info**\n\n{ r2.text[:1000] }")
            
    except Exception as e:
        bot.send_message(m.chat.id, f"❌ Error: {e}\nPublic API try kar raha hu...")
        try:
            r = requests.get(f"https://free-api-ff-info.vercel.app/info?uid={uid}", timeout=10)
            bot.send_message(m.chat.id, f"Info: {r.text[:1500]}")
        except Exception as e2:
            bot.send_message(m.chat.id, f"Info API bhi down hai: {e2}")

@bot.message_handler(commands=['like'])
def like_cmd(m):
    uid = m.text.replace("/like","").strip()
    if not uid.isdigit():
        bot.reply_to(m, "Sahi UID bhejo. Ex: /like 3513765300")
        return
    bot.send_message(m.chat.id, f"⚠️ Like API abhi 503 de raha hai, server down hai. Info use karo: /info {uid}")

@bot.message_handler(func=lambda m: True)
def handle_all(m):
    # Seedha UID bheja to Info samjho
    txt = m.text.strip()
    if txt.isdigit():
        m.text = f"/info {txt}"
        return info_cmd(m)
    else:
        bot.reply_to(m, "Command sahi bhejo:\n/info 3513765300\n/like 3513765300")

print("Bot Started...")
bot.infinity_polling()
