# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import (
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
    FORCE_SUB_5,
    FORCE_SUB_6,
)
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if (
        not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    if (
        FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    if (
        FORCE_SUB_2
        and not FORCE_SUB_1
        and not FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪɪ", url=invitelink2),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    if (
        FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪɪɪ", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    if (
        FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪᴠ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    # Flexiable 2 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪ", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪɪ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons

    # Flexiable 2 Subs CH
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and not FORCE_SUB_2
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪ", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪɪ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons

    # Flexiable 3 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    # Flexiable 4 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    # Flexiable 5 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    # Flexiable 6 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and FORCE_SUB_5
        and FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons


def fsub_button(client, message):
    if (
        FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    if (
        FORCE_SUB_2
        and not FORCE_SUB_1
        and not FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪɪ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    if (
        FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    if (
        FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    # Flexiable 2 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪ", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪɪ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    # Flexiable 2 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and not FORCE_SUB_2
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪ", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ɪɪ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    # Flexiable 3 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    # Flexiable 4 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 4", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    # Flexiable 5 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and FORCE_SUB_5
        and not FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 4", url=client.invitelink4),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 5", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    # Flexiable 6 Subs
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and FORCE_SUB_5
        and FORCE_SUB_6
    ):
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 4", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 5", url=client.invitelink5),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 6", url=client.invitelink6),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
