from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "AutoFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def handler(client, message):
    if message.text == "/start":
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🎬 Movies", callback_data="movies"),
                InlineKeyboardButton("⭐ VIP", callback_data="vip")
            ],
            [
                InlineKeyboardButton("📺 Series", callback_data="series")
            ]
        ])

        await message.reply_text(
            "🎥 Advanced Auto Filter Bot Running Successfully!",
            reply_markup=buttons
        )

print("Bot Started")
app.run()
