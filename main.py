
import os
import asyncio
from threading import Thread
from flask import Flask
from telethon import TelegramClient, events

app = Flask(__name__)

@app.route("/")
def home():
    return "not_bot is running!"

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
PORT = int(os.getenv("PORT", "10000"))

client = TelegramClient("not_bot", API_ID, API_HASH)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.ping"))
async def ping(event):
    await event.edit("🏓 not_bot فعاله!")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.help"))
async def help_command(event):
    await event.edit(
        "🇮🇷 پنل مدیریت not_bot\n\n"
        ".ping - تست اتصال\n"
        ".help - راهنما"
    )

def run_web():
    app.run(host="0.0.0.0", port=PORT)

async def run_telegram():
    await client.start()
    print("Telegram connected")
    await client.run_until_disconnected()

if __name__ == "__main__":
    Thread(target=run_web, daemon=True).start()
    asyncio.run(run_telegram())
    
