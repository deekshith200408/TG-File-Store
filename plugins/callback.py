import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
OWNER_ID = os.environ.get("OWNER_ID")


@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """💡🅱🅾🆃🆂 🅷🅴🅻🅿 :-

👾 Jᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ғɪʟᴇs ɪ ᴡɪʟʟ sᴛᴏʀᴇ ғɪʟᴇ ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜ sʜᴀʀᴇ ᴀʙʟᴇ ʟɪɴᴋ.

[ΝϴͲᎬ :- 𝗬𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲 𝗺𝗲 𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝘁𝗼𝗼]✓🥳

🧭 Mᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪssɪᴏɴ.🎨
°~° Tʜᴀᴛs ᴇɴᴏᴜɢʜ ɴᴏᴡ ᴄᴏɴᴛɪɴᴜᴇ ᴜᴘʟᴏᴀᴅɪɴɢ ғɪʟᴇs ɪɴ ᴄʜᴀɴɴᴇʟ ɪ ᴡɪʟʟ ᴇᴅɪᴛ ᴀʟʟ ᴘᴏsᴛs ᴀɴᴅ ᴀᴅᴅ sʜᴀʀᴇ ᴀʙʟᴇ ʟɪɴᴋ ᴜʀʟ ʙᴜᴛᴛᴏɴs.🤹

© [ᴜɴɪ ᴍᴏᴠɪᴇs ʙᴏx](https://t.me/UNI_MOVIES_BOX).

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('𝙶𝙾 𝙷𝙾𝙼𝙴 🏕', callback_data='home'),
            InlineKeyboardButton('𝙰𝙱𝙾𝚄𝚃 𝙱𝙾𝚃 📕', callback_data='about')
        ],
        [
            InlineKeyboardButton('𝙲𝙻𝙾𝚂𝙴 𝙰𝙻𝙻 🔐', callback_data='close')
        ]
    ]

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


@Client.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    owner = await c.get_users(int(OWNER_ID))
    bot = await c.get_me()

    # about text
    about_text = f"""🤴 𝐀𝐁𝐎𝐔𝐓 𝐁𝐎𝐓:~~

🤖 𝐌𝐲 𝐍𝐚𝐦𝐞: {bot.mention(style='md')}
    
📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: [ᴘʏᴛʜᴀɴ 3](https://www.python.org/)

🧰 𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤: [ᴘʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)

👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: [𝙳𝙴𝙴𝙺𝚂𝙷𝙸𝚃𝙷](https://t.me/Deeks_04_8)

📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: [ᴜᴍʀ ᴋᴀɴɴᴀᴅᴀ ᴍᴏᴠɪᴇs](https://t.me/UMR_KAN_MOVIES)

👥 𝐆𝐫𝐨𝐮𝐩: [ᴜɴɪᴠᴇʀsᴀʟ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛs](https://t.me/UM_Requests)

© [𝚄𝙽𝙸 𝙼𝙾𝚅𝙸𝙴𝚂 𝙱𝙾𝚇](https://t.me/UNI_MOVIES_BOX)

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•
"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('𝙶𝙾 𝙷𝙾𝙼𝙴 🏕', callback_data='home'),
            InlineKeyboardButton('𝙷𝙴𝙻𝙿 💡', callback_data='help')
        ],
        [
            InlineKeyboardButton('𝙲𝙻𝙾𝚂𝙴 𝙰𝙻𝙻 🔐', callback_data='close')
        ]
    ]

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)
