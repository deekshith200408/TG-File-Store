import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")



#################################### FOR PRIVATE ################################################
@Client.on_message((filters.document|filters.video|filters.audio) & filters.incoming & ~filters.edited & ~filters.channel)
async def storefile(c, m):

    if m.document:
       media = m.document
    if m.video:
       media = m.video
    if m.audio:
       media = m.audio

    # text
    text = "--**🗃️ 𝐅𝐈𝐋𝐄 𝐃𝐈𝐓𝐀𝐈𝐋𝐒:**--\n\n\n"
    text += f"📂 __𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴:__ `{media.file_name}`\n\n"
    text += f"💽 __𝙼𝙸𝙼𝙴 𝚃𝚈𝙿𝙴:__ `{media.mime_type}`\n\n"
    text += f"📊 __𝙵𝙸𝙻𝙴 𝚂𝙸𝚉𝙴:__ `{humanbytes(media.file_size)}`\n\n"
    if not m.document:
        text += f"🎞 __𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽:__ `{TimeFormatter(media.duration * 1000)}`\n\n" if media.duration else ""
        if m.audio:
            text += f"🎵 __𝚃𝙸𝚃𝙸𝙻𝙴:__ `{media.title}`\n\n" if media.title else ""
            text += f"🎙 __𝙿𝙴𝚁𝙵𝙾𝚁𝙼𝙴𝚁:__ `{media.performer}`\n\n" if media.performer else ""
    text += f"__✏ 𝙲𝙰𝙿𝚃𝙸𝙾𝙽:__ `{m.caption}`\n\n"
    text += "**--𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒:--**\n\n\n"
    text += f"__🦚 ғɪᴛsᴛ ɴᴀᴍᴇ:__ `{m.from_user.first_name}`\n\n"
    text += f"__🐧 ʟᴀsᴛ ɴᴀᴍᴇ:__ `{m.from_user.last_name}`\n\n" if m.from_user.last_name else ""
    text += f"__👁 ᴜsᴇʀɴᴀᴍᴇ:__ @{m.from_user.username}\n\n" if m.from_user.username else ""
    text += f"__👤 ᴜsᴇʀ ɪᴅ:__ `{m.from_user.id}`\n\n"
    text += f"__💬 ᴅᴄ ɪᴅ:__ {m.from_user.dc_id}\n\n" if m.from_user.dc_id else ""

    # if databacase channel exist forwarding message to channel
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))
        await msg.reply(text)

    # creating urls
    bot = await c.get_me()
    url = f"https://t.me/{bot.username}?start={m.chat.id}_{m.message_id}" if not DB_CHANNEL_ID else f"https://t.me/{bot.username}?start={m.chat.id}_{msg.message_id}"
    txt = text.replace(' ', '%20').replace('\n', '%0A').replace('--', '')
    share_url = f"tg://share?url={txt}File%20Link%20👉%20{url}"

    # making buttons
    buttons = [[
        InlineKeyboardButton(text="𝐎𝐏𝐄𝐍 𝐔𝐑𝐋 🔗", url=url),
        InlineKeyboardButton(text="𝐒𝐇𝐀𝐑𝐄 𝐋𝐈𝐍𝐊 👤", url=share_url)
    ]]

    # sending message
    await m.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

#################################### FOR CHANNEL################################################

@Client.on_message((filters.document|filters.video|filters.audio) & filters.incoming & filters.channel & ~filters.edited)
async def storefile_channel(c, m):

    if m.document:
       media = m.document
    if m.video:
       media = m.video
    if m.audio:
       media = m.audio

    # text
    text = "**🗃️ 𝐃𝐄𝐓𝐀𝐈𝐋𝐒:**\n\n\n"
    text += f"📂 __𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴:__ `{media.file_name}`\n\n"
    text += f"💽 __𝙼𝙸𝙼𝙴 𝚃𝚈𝙿𝙴:__ `{media.mime_type}`\n\n"
    text += f"📊 __𝙵𝙸𝙻𝙴 𝚂𝙸𝚉𝙴:__ `{humanbytes(media.file_size)}`\n\n"
    if not m.document:
        text += f"🎞 __𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽:__ `{TimeFormatter(media.duration * 1000)}`\n\n" if media.duration else ""
        if m.audio:
            text += f"🎵 __𝚃𝙸𝚃𝙻𝙴:__ `{media.title}`\n\n" if media.title else ""
            text += f"🎙 __𝙿𝙴𝚁𝙵𝙾𝚁𝙼𝙴𝚁:__ `{media.performer}`\n\n" if media.performer else ""
    text += f"__✏ 𝙲𝙰𝙿𝚃𝙸𝙾𝙽:__ `{m.caption}`\n\n"
    text += "**𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒:**\n\n\n"
    text += f"__📢 ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:__ `{m.chat.title}`\n\n"
    text += f"__🗣 ᴜsᴇʀ ɴᴀᴍᴇ:__ @{m.chat.username}\n\n" if m.chat.username else ""
    text += f"__👤 ᴄʜᴀɴɴᴇʟ ɪᴅ:__ `{m.chat.id}`\n\n"
    text += f"__💬 ᴅᴄ ɪᴅ:__ {m.chat.dc_id}\n\n" if m.chat.dc_id else ""
    text += f"__👁 ᴍᴇᴍʙᴇʀ ᴄᴏᴜɴᴛ:__ {m.chat.members_count}\n\n" if m.chat.members_count else ""

    # if databacase channel exist forwarding message to channel
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))
        await msg.reply(text)

    # creating urls
    bot = await c.get_me()
    url = f"https://t.me/{bot.username}?start={m.chat.id}_{m.message_id}" if not DB_CHANNEL_ID else f"https://t.me/{bot.username}?start={m.chat.id}_{msg.message_id}"
    txt = text.replace(' ', '%20').replace('\n', '%0A')
    share_url = f"tg://share?url={txt}File%20Link%20👉%20{url}"

    # making buttons
    buttons = [[
        InlineKeyboardButton(text="𝐎𝐏𝐄𝐍 𝐔𝐑𝐋🔗", url=url),
        InlineKeyboardButton(text="𝐒𝐇𝐀𝐑𝐄 𝐋𝐈𝐍𝐊👤", url=share_url)
    ]]

    # Editing and adding the buttons
    await m.edit_reply_markup(InlineKeyboardMarkup(buttons))


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " days, ") if days else "") + \
        ((str(hours) + " hrs, ") if hours else "") + \
        ((str(minutes) + " min, ") if minutes else "") + \
        ((str(seconds) + " sec, ") if seconds else "") + \
        ((str(milliseconds) + " millisec, ") if milliseconds else "")
    return tmp[:-2]
