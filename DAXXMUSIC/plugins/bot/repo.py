from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗠𝗿 𝗕𝗿𝗼𝗸𝗲𝗻'𝘀 𝗿𝗲𝗽𝗼 ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀ𝘀ɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪ𝘀𝘀ᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪ𝘀𝘀ᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏ𝘀 ✰
 
 ➲ ʀᴜɴ 𝟮𝟰𝘅𝟳 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ 𝘀ᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ 𝘀ᴇɴᴅ 𝘀𝘀
**"""




@app.on_message(filters.command("rxpx"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/+u6mIC9k6FhozYTM9"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/mrbrokn"),
          ],
               [
                InlineKeyboardButton("𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/Brokenxnetwork"),

],
[
              InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟︎", url=f"https://github.com/MRBROKEN/BANALL"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/MRBROKEN/proai"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://github.com/MRBROKEN/YumikooRobot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/MRBROKEN/CHATBOT"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com/MRBROKEN/STRINGBOT"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧𝗚𝗣𝗧", url=f"https://github.com/MRBROKEN/CHATGPT"),
],
[
              InlineKeyboardButton("𝗩𝗣𝗦", url=f"https://github.com/MRBROKEN/Kaali-Linux"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://github.com/MRBROKEN/MOVIEBOT"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://github.com/MRBROKEN/STRINGHACK"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/MRBROKEN/IDCHAT"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/MRBROKEN/USERBOT"),
InlineKeyboardButton("𝗦𝗘𝗔𝗥𝗖𝗛𝗕𝗢𝗧", url=f"https://github.com/MRBROKEN/SEARCH_BOT"),
],
[
InlineKeyboardButton("𝗖𝗖 𝗕𝗢𝗧", url=f"https://github.com/MRBROKEN/CC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/22929baacd6f08f0dc08b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("rxpx", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/MRBROKEN/MUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/+u6mIC9k6FhozYTM9)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
