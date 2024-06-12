import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from DAXXMUSIC import app

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(client: Client, message: Message):
    try:
        if message.sender_chat or not await check_pretender(message.chat.id):
            return

        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        if not await usr_data(user_id):
            await add_userdata(user_id, username, first_name, last_name)
            return

        username_before, first_name_before, last_name_before = await get_userdata(user_id)
        msg = ""

        if username_before != username or first_name_before != first_name or last_name_before != last_name:
            msg += f"""
**🔓 Pretender Detected 🔓**
➖➖➖➖➖➖➖➖➖➖➖➖
**🍊 Name**: {message.from_user.mention}
**🍅 User ID**: {user_id}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""

        if username_before != username:
            username_before = f"@{username_before}" if username_before else "No Username"
            username_after = f"@{username}" if username else "No Username"
            msg += f"""
**🐻‍❄️ Changed Username 🐻‍❄️**
➖➖➖➖➖➖➖➖➖➖➖➖
**🎭 From**: {username_before}
**🍜 To**: {username_after}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""

        if first_name_before != first_name:
            msg += f"""
**🪧 Changed First Name 🪧**
➖➖➖➖➖➖➖➖➖➖➖➖
**🔐 From**: {first_name_before}
**🍓 To**: {first_name}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""

        if last_name_before != last_name:
            last_name_before = last_name_before or "No Last Name"
            last_name_after = last_name or "No Last Name"
            msg += f"""
**🪧 Changed Last Name 🪧**
➖➖➖➖➖➖➖➖➖➖➖➖
**🚏 From**: {last_name_before}
**🍕 To**: {last_name_after}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""

        if msg:
            await message.reply_photo("https://telegra.ph/file/6b0a0f76bf5660454ae89.jpg", caption=msg)
            await add_userdata(user_id, username, first_name, last_name)

    except Exception as e:
        logger.error(f"Error in chk_usr: {e}")

@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(client: Client, message: Message):
    try:
        if len(message.command) == 1:
            await message.reply("**Detect pretender users usage: pretender on|off**")
            return

        command = message.command[1]
        chat_id = message.chat.id
        chat_title = message.chat.title

        if command == "enable":
            if await impo_on(chat_id):
                await message.reply("**Pretender mode is already enabled.**")
            else:
                await impo_on(chat_id)
                await message.reply(f"**Successfully enabled pretender mode for {chat_title}**")

        elif command == "disable":
            if not await impo_off(chat_id):
                await message.reply("**Pretender mode is already disabled.**")
            else:
                await impo_off(chat_id)
                await message.reply(f"**Successfully disabled pretender mode for {chat_title}**")

        else:
            await message.reply("**Detect pretender users usage: pretender on|off**")

    except Exception as e:
        logger.error(f"Error in set_mataa: {e}")

if __name__ == "__main__":
    app.run()
