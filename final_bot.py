import telebot, requests, time
BOT_TOKEN = "8994456344:AAF-CPxn9nZNmjRv92BrP1h8lsw3uGV_OJI"
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjo3Nzk5MTAzNTMyLCJuaWNrbmFtZSI6ImZEZDNiV3R3VnkxVUR3PT0iLCJub3RpX3JlZ2lvbiI6IklORCIsImxvY2tfcmVnaW9uIjoiSU5EIiwiZXh0ZXJuYWxfaWQiOiJjOWQ3YjkzMGY3N2M5NTc0NTA2NTlkZDQ0ZmU2OTRkZiIsImV4dGVybmFsX3R5cGUiOjgsInBsYXRfaWQiOjEsImNsaWVudF92ZXJzaW9uIjoiMi4xMzIuNCIsImNsaWVudF92ZXJzaW9uX2NvZGUiOiIyMDE5MTE4NTI1IiwiZW11bGF0b3Jfc2NvcmUiOjEwMCwiaXNfZW11bGF0b3IiOnRydWUsImNvdW50cnlfY29kZSI6IlNFIiwiZXh0ZXJuYWxfdWlkIjoxODM1MDAwODgxMDQwLCJyZWdfYXZhdGFyIjoxMDIwMDAwMDUsInNvdXJjZSI6MCwibG9ja19yZWdpb25fdGltZSI6MTY4NTIwOTMyOSwiY2xpZW50X3R5cGUiOjIsInNpZ25hdHVyZV9tZDUiOiIxYWM0YjgwZWNmMDQ3OGE0NDIwM2JmOGZhYzYxMjBmNSIsInVzaW5nX3ZlcnNpb24iOjIsInJlbGVhc2VfY2hhbm5lbCI6ImFuZHJvaWRfbWF4IiwicmVsZWFzZV92ZXJzaW9uIjoiT0I1NSIsImV4cCI6MTc5MDUxOTAwM30.CQWIE2KtBJAprKn0nRDXwZ9kCZK-EMc7QfWoA3yR5nY"
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 FF Like Bot Ready!\n\nCommand:\n/like 3513765300\n\nYa seedha UID bhejo.")
@bot.message_handler(func=lambda m: True)
def handle(m):
    uid = m.text.replace("/like","").strip()
    if not uid.isdigit(): 
        bot.reply_to(m, "Sahi UID bhejo. Example: 3513765300")
        return
    bot.send_message(m.chat.id, f"⏳ {uid} pe like bhej raha hu...")
    for i in range(3):
        try:
            headers = {"Authorization": f"Bearer {JWT_TOKEN}","Content-Type":"application/json"}
            r = requests.post("https://client.ind.freefiremobile.com/LikeProfile", headers=headers, json={"uid": uid}, timeout=10)
            bot.send_message(m.chat.id, f"Attempt {i+1}: {r.text[:500]}")
            time.sleep(2)
        except Exception as e:
            bot.send_message(m.chat.id, f"Error: {e}")
            break
print("Bot Started... Telegram pe /start bhejo")
bot.infinity_polling()
