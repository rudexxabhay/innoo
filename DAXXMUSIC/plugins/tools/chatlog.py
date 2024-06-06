import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app  

photo = [
    "https://telegra.ph/file/98afc0c330924c0321100.jpg",
    "https://telegra.ph/file/bc83d63ca11e03deef273.jpg",
    "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg",
    "https://te.legra.ph/file/6298d377ad3eb46711644.jpg",
    "https://telegra.ph/file/56d1760224589ee370186.jpg",
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg"
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}\n\n"
                f"**★ᴍᴀᴅᴇ ʙʏ ᴍʀ ʙʀᴏᴋᴇɴ★**\n\n"
                f"____________________________________"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome
@app.on_message(filters.command("wel") & ~filters.private)
@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
              f"**❅────✦ ᴡᴇʟᴄᴏᴍᴇ ✦────❅**\n\n"
              f"▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
              f"**➻ ɴᴀᴍᴇ »** {user.mention}\n"
              f"**➻ ɪᴅ »** `{user.id}\n"
              f"**➻ ᴜ_ɴᴀᴍᴇ »** @{user.username}\n"
              f"**➻ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs »** {count}\n"
              f"**★ᴍᴀᴅᴇ ʙʏ ᴍʀ ʙʀᴏᴋᴇɴ★**\n\n"
              f"▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"    
              f"**❅─────✧❅✦❅✧─────❅**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴄʜᴏᴏsᴇ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))


