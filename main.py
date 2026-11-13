
import os
import asyncio
from threading import Thread
from flask import Flask
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

app = Flask(__name__)

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

@app.route("/")
def home():
    return "not_bot is running!"

async def main():
    if not API_ID or not API_HASH or not SESSION:
        raise ValueError("API_ID, API_HASH or SESSION is missing")

    client = TelegramClient(
        StringSession(SESSION),
        int(API_ID),
        API_HASH
    )

    @client.on(events.NewMessage(outgoing=True, pattern=r"\.panel"))
    async def panel(event):
        await event.respond(
            "🇮🇷 **پنل مدیریت not_bot**\n\n"
            "به پنل خوش آمدی. یک بخش را انتخاب کن:",
            buttons=[
                [Button.inline("📊 وضعیت اتصال", b"status")],
                [Button.inline("📖 راهنما", b"help")],
                [Button.inline("⚙️ تنظیمات", b"settings")]
            ]
        )

    @client.on(events.CallbackQuery)
    async def callbacks(event):
        if event.data == b"status":
            await event.answer("اتصال برقرار است ✅", alert=True)

        elif event.data == b"help":
            await event.answer(
                "دستورها:\n.panel - پنل مدیریت\n.ping - تست اتصال",
                alert=True
            )

        elif event.data == b"settings":
            await event.answer(
                "بخش تنظیمات به‌زودی اضافه می‌شود.",
                alert=True
            )

    @client.on(events.NewMessage(outgoing=True, pattern=r"\.ping"))
    async def ping(event):
        await event.edit("🏓 not_bot فعاله!")

    await client.start()
    print("not_bot connected!")
    await client.run_until_disconnected()

def run_web():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

if __name__ == "__main__":
    Thread(target=run_web, daemon=True).start()
    asyncio.run(main())
    
