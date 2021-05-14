import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")
OWNER_ID = os.environ.get("OWNER_ID")


@Client.on_message(filters.command('start') & filters.incoming & filters.private)
async def start(c, m, cb=False):
    owner = await c.get_users(int(OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""🤓🤹ʜɪ ʜᴇʟᴏo, {m.from_user.mention(style='md')}

💡 ** ɪ ᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ**

Yᴏᴜ ᴄᴀɴ sᴛᴏʀᴇ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Mᴇᴅɪᴀ ғᴏʀ ᴘᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ!

🧬ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ /help....🔭

🏛️𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚘𝚠𝚗𝚎𝚍 :- © [𝗨𝗡𝗜 𝗠𝗢𝗩𝗜𝗘𝗦 𝗕𝗢𝗫](url:https://t.me/UNI_MOVIES_BOX).

🔬🧲© ᴄʀᴇᴀᴛᴏʀ : @Deeks_04_8🎩,

°•°•°•°•°•°•°•°•[ 🆄🅼🆁 ]°•°•°•°•°•°•°•°•}
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('🤹𝐜𝐫𝐞𝐚𝐭𝐞𝐫/𝐦𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐫🤴', url=f"https://t.me/{owner_username}")],
            [InlineKeyboardButton('Help 💡', callback_data="help")
        ,
        
            InlineKeyboardButton('About 📕', callback_data="about")
        ],[InlineKeyboardButton('🎪𝐉𝐎𝐈𝐍 𝐎𝐔𝐑𝐒 𝐀𝐋𝐋 𝐂𝐇𝐀𝐍𝐍𝐄𝐋𝐒🎪', url=f"https://t.me/UNI_MOVIES_BOX")
    ]

    # when button home is pressed
    if cb:
        return await m.message.edit(
                   text=text,
                   reply_markup=InlineKeyboardMarkup(buttons)
               )

    if len(m.command) > 1: # sending the stored file
        chat_id, msg_id = m.command[1].split('_')
        msg = await c.get_messages(int(chat_id), int(msg_id)) if not DB_CHANNEL_ID else await c.get_messages(int(DB_CHANNEL_ID), int(msg_id))

        if msg.empty:
            owner = await c.get_users(int(OWNER_ID))
            return await m.reply_text(f"🥴 Sorry bro your file was missing\n\nPlease contact my owner 👉 {owner.mention(style='md')}")
        
        caption = f"{msg.caption.markdown}\n\n\n" if msg.caption else ""

        if chat_id.startswith('-100'): #if file from channel
            channel = await c.get_chat(int(chat_id))
            caption += "**--𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒:--**\n\n"
            caption += f"__🎪 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙽𝙰𝙼𝙴:__ `{channel.title}`\n\n"
            caption += f"__🕵️ 𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴:__ @{channel.username}\n\n" if channel.username else ""
            caption += f"__🆔 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙳:__ `{channel.id}`\n\n"
            caption += f"__💬 𝙳𝙲 𝙸𝙳:__ {channel.dc_id}\n\n" if channel.dc_id else ""
            caption += f"__💠 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙲𝙾𝚄𝙽𝚃:__ {channel.members_count}\n\n" if channel.members_count else ""

        else: #if file not from channel
            user = await c.get_users(int(chat_id))
            caption += "\n\n\n**--𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒:--**\n\n"
            caption += f"__🤹 𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴:__ `{user.first_name}`\n\n"
            caption += f"__🙄 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴:__ `{user.last_name}`\n\n" if user.last_name else ""
            caption += f"__♨️ 𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴:__ @{user.username}\n\n" if user.username else ""
            caption += f"__💺 𝚄𝚂𝙴𝚁 𝙸𝙳:__ `{user.id}`\n\n"
            caption += f"__💬 𝙳𝙲 𝙸𝙳:__ {user.dc_id}\n\n" if user.dc_id else ""

        await msg.copy(m.from_user.id, caption=caption)


    else: # sending start message
        await m.reply_text(
            text=text,
            quote=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )


@Client.on_message(filters.command('me') & filters.incoming & filters.private)
async def me(c, m):
    me = await c.get_users(m.from_user.id)
    text = "--**𝐘𝐎𝐔𝐑𝐒 𝐃𝐄𝐓𝐀𝐈𝐋𝐒:**--\n\n\n"
    text += f"__🦚 𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴:__ `{me.first_name}`\n\n"
    text += f"__🐧 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴:__ `{me.last_name}`\n\n" if me.last_name else ""
    text += f"__👁 𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴:__ @{me.username}\n\n" if me.username else ""
    text += f"__👤 𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴:__ `{me.id}`\n\n"
    text += f"__💬 𝙳𝙲 𝙸𝙳:__ {me.dc_id}\n\n" if me.dc_id else ""
    text += f"__✔ ɪs ᴠᴇʀɪғɪᴇᴅ ᴀs ᴛᴇʟᴇɢʀᴀᴍᴇ:__ `{me.is_verified}`\n\n" if me.is_verified else ""
    text += f"__👺 𝙸𝚂 𝙵𝙰𝙺𝙴:__ {me.is_fake}\n\n" if me.is_fake else ""
    text += f"__💨 𝙸𝚂 𝚂𝙲𝙰𝙼:__ {me.is_scam}\n\n" if me.is_scam else ""
    text += f"__📃 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 𝙲𝙾𝙳𝙴:__ {me.language_code}\n\n" if me.language_code else ""

    await m.reply_text(text, quote=True)
