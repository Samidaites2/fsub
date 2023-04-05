# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from bot import Bot
from config import (
    ADMINS,
    CUSTOM_CAPTION,
    DISABLE_CHANNEL_BUTTON,
    FORCE_MSG,
    LOGGER,
    PROTECT_CONTENT,
    START_MSG,
)
from database.sql import add_user, full_userbase
from pyrogram import filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.types import InlineKeyboardMarkup, Message

from helper_func import (
    decode,
    get_messages,
    subsfour,
    subsfours,
    subsfives,
    subssixs,
    subsone,
    subsonetwo,
    subsonetri,
    subsonetwotri,
    substri,
    substwo,
)

from .button import fsub_button, start_button


@Bot.on_message(
    filters.command("start")
    & filters.private
    & subsone
    & substwo
    & substri
    & subsfour
    & subsonetwo
    & subsonetri
    & subsonetwotri
    & subsfours
    & subsfives
    & subssixs
)
async def start_command(client: Bot, message: Message):
    id = message.from_user.id
    user_name = "@" + message.from_user.username if message.from_user.username else None
    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except BaseException:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except BaseException:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except BaseException:
                return
        temp_msg = await message.reply("<code>Tunggu Sebentar...</code>")
        try:
            messages = await get_messages(client, ids)
        except BaseException:
            await message.reply_text("<b>Telah Terjadi Error </b>🥺")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(
                    previouscaption="" if not msg.caption else msg.caption.html,
                    filename=msg.document.file_name,
                )
            else:
                caption = "" if not msg.caption else msg.caption.html

            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None
            try:
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode="html",
                    protect_content=PROTECT_CONTENT,
                    reply_markup=reply_markup,
                )
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode="html",
                    protect_content=PROTECT_CONTENT,
                    reply_markup=reply_markup,
                )
            except BaseException:
                pass
    else:
        out = start_button(client)
        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None
                if not message.from_user.username
                else "@" + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(out),
            disable_web_page_preview=True,
            quote=True,
        )

    return


@Bot.on_message(filters.command("start") & filters.private)
async def not_joined(client: Bot, message: Message):
    buttons = fsub_button(client, message)
    try:
        await message.reply(
            text=FORCE_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None
                if not message.from_user.username
                else "@" + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True,
            disable_web_page_preview=True,
        )
    except InputUserDeactivated:
        pass
    except UserIsBlocked:
        pass
    except PeerIdInvalid:
        pass
    except Exception as e:
        LOGGER(__name__).warning(e)


@Bot.on_message(filters.command(["users", "stats"]) & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(
        chat_id=message.chat.id, text="<code>Processing ...</code>"
    )
    users = await full_userbase()
    await msg.edit(f"{len(users)} <b>Pengguna menggunakan bot ini</b>")
