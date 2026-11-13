import os
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = "not_bot"

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.ping"))
async def ping(event):
    await event.edit("🏓 ربات فعاله!")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.help"))
async def help_command(event):
    await event.edit(
        "🇮🇷 پنل مدیریت not_bot\n\n"
        ".ping - تست اتصال\n"
        ".help - راهنما"
    )

async def main():
    print("not_bot started")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
