import requests

URL = "http://127.0.0.1:5000/chat"

print("Type 'exit' to quit")

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break

    try:
        r = requests.post(URL, json={"message": msg}, timeout=60)
        print("Bot:", r.json()["reply"])
    except Exception as e:
        print("❌ Server not running. Start with: python app.py")
