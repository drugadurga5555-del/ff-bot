import requests
TOKEN = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjo3Nzk5MTAzNTMyLCJuaWNrbmFtZSI6ImZEZDNiV3R3VnkxVUR3PT0iLCJub3RpX3JlZ2lvbiI6IklORCIsImxvY2tfcmVnaW9uIjoiSU5EIiwiZXh0ZXJuYWxfaWQiOiJjOWQ3YjkzMGY3N2M5NTc0NTA2NTlkZDQ0ZmU2OTRkZiIsImV4dGVybmFsX3R5cGUiOjgsInBsYXRfaWQiOjEsImNsaWVudF92ZXJzaW9uIjoiMi4xMzIuNCIsImNsaWVudF92ZXJzaW9uX2NvZGUiOiIyMDE5MTE4NTI1IiwiZW11bGF0b3Jfc2NvcmUiOjEwMCwiaXNfZW11bGF0b3IiOnRydWUsImNvdW50cnlfY29kZSI6IlNFIiwiZXh0ZXJuYWxfdWlkIjoxODM1MDAwODgxMDQwLCJyZWdfYXZhdGFyIjoxMDIwMDAwMDUsInNvdXJjZSI6MCwibG9ja19yZWdpb25fdGltZSI6MTY4NTIwOTMyOSwiY2xpZW50X3R5cGUiOjIsInNpZ25hdHVyZV9tZDUiOiIxYWM0YjgwZWNmMDQ3OGE0NDIwM2JmOGZhYzYxMjBmNSIsInVzaW5nX3ZlcnNpb24iOjIsInJlbGVhc2VfY2hhbm5lbCI6ImFuZHJvaWRfbWF4IiwicmVsZWFzZV92ZXJzaW9uIjoiT0I1NSIsImV4cCI6MTc5MDUxOTAwM30.CQWIE2KtBJAprKn0nRDXwZ9kCZK-EMc7QfWoA3yR5nY"
UID = "3513765300"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

print(f"Sending like to {UID}...")
try:
    r = requests.post("https://client.ind.freefiremobile.com/LikeProfile", headers=headers, json={"uid": UID}, timeout=15)
    print("Response:", r.text)
    if "success" in r.text.lower() or r.status_code == 200:
        print("\n✅ Like Bhej Diya!")
    else:
        print("\n❌ Fail Ho Gaya - Token expire ho sakta hai")
except Exception as e:
    print("Error:", e)
