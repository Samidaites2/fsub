# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from bot import Bot
from config import ADMINS, PROTECT_CONTENT
from database.sql import query_msg
from pyrogram import filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked
from pyrogram.types import Message


@Bot.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply(
            "<code>Broadcasting Message Tunggu Sebentar...</code>"
        )
        for row in query:
            chat_id = int(row[0])
            if chat_id not in ADMINS:
                try:
                    await broadcast_msg.copy(chat_id, protect_content=PROTECT_CONTENT)
                    successful += 1
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await broadcast_msg.copy(chat_id, protect_content=PROTECT_CONTENT)
                    successful += 1
                except UserIsBlocked:
                    blocked += 1
                except InputUserDeactivated:
                    deleted += 1
                except BaseException:
                    unsuccessful += 1
                total += 1
        status = f"""<b><u>Berhasil Broadcast</u>
Jumlah Pengguna: <code>{total}</code>
Berhasil: <code>{successful}</code>
Gagal: <code>{unsuccessful}</code>
Pengguna diblokir: <code>{blocked}</code>
Akun Terhapus: <code>{deleted}</code></b>"""
        return await pls_wait.edit(status)
    else:
        msg = await message.reply(
            "<code>Gunakan Perintah ini Harus Sambil Reply ke pesan telegram yang ingin di Broadcast.</code>"
        )
        await asyncio.sleep(8)
        await msg.delete()
