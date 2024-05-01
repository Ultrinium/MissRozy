# (c) @LazyDeveloperr

import asyncio
from configs import Config
from configs import *
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size

async def reply_forward(message: Message, file_id: int):

    try:
        await message.reply_text(
            f"**ʜᴇʀᴇ ɪꜱ ꜱʜᴀʀᴀʙʟᴇ ʟɪɴᴋ ᴏꜰ ᴛʜɪꜱ ꜰɪʟᴇ:**\n"
            f"https://t.me/{Config.BOT_USERNAME}?start=LazyDeveloperr_{str_to_b64(str(file_id))}\n"
            f"__ᴛᴏ ʀᴇᴛʀɪᴠᴇ ᴛʜᴇ ꜱᴛᴏʀᴇᴅ ꜰɪʟᴇ, ᴊᴜꜱᴛ ᴏᴘᴇɴ ᴛʜᴇ ʟɪɴᴋ !__\n\n",
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await reply_forward(message, file_id)



