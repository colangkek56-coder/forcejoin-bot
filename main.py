from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

CHANNEL_USERNAME = "outfitind"

app = Client("forcejoinbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    
    try:
        member = await client.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            
            if len(message.command) > 1:
                param = message.command[1]
                if param == "belovedthif":
                    await message.reply("🔥 Akses diterima! Ini kontennya...")
                else:
                    await message.reply("✅ Kamu sudah join!")
            else:
                await message.reply("✅ Kamu sudah join!")
                
        else:
            raise Exception("Belum join")
            
    except:
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔔 Join Channel", url="https://t.me/outfitind")],
            [InlineKeyboardButton("🔄 Saya Sudah Join", callback_data="cek_join")]
        ])
        
        await message.reply(
            "❌ Kamu wajib join channel dulu.",
            reply_markup=buttons
        )

@app.on_callback_query()
async def callback(client, callback_query):
    user_id = callback_query.from_user.id
    
    try:
        member = await client.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await callback_query.message.edit_text("✅ Berhasil! Sekarang kirim ulang /start")
        else:
            raise Exception("Belum join")
    except:
        await callback_query.answer("Masih belum join 😅", show_alert=True)

app.run()
