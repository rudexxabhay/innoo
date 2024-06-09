import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("mmf"))
async def mmf(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if not reply_message or not reply_message.photo:
        await message.reply_text("**Reply to an image with /mmf to memify it.**")
        return

    if len(message.text.split()) < 2:
        await message.reply_text("**Give me text after /mmf to memify.**")
        return

    msg = await message.reply_text("**Memifying this image! ✊🏻**")
    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    try:
        meme = await drawText(file, text)
        await app.send_document(chat_id, document=meme)
    except Exception as e:
        await message.reply_text(f"**Failed to memify image. Error: {e}**")
    finally:
        await msg.delete()
        if os.path.exists(meme):
            os.remove(meme)

async def drawText(image_path, text):
    try:
        img = Image.open(image_path)
        os.remove(image_path)  # Remove the downloaded image file
    except Exception as e:
        raise Exception(f"Error opening image: {e}")

    i_width, i_height = img.size

    if os.name == "nt":
        fnt = "arial.ttf"
    else:
        fnt = "./DAXXMUSIC/assets/default.ttf"

    try:
        m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    except Exception as e:
        raise Exception(f"Error loading font: {e}")

    upper_text, lower_text = (text.split(";") + [""])[:2]  # Split and handle missing lower text

    draw = ImageDraw.Draw(img)

    current_h, pad = 10, 5

    def draw_text_wrapped(draw, text, width, font, pos_y):
        for line in textwrap.wrap(text, width=width):
            u_width, u_height = font.getsize(line)
            x_pos = (i_width - u_width) / 2
            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:  # Outline
                draw.text((x_pos + dx, pos_y + dy), line, font=font, fill=(0, 0, 0))
            draw.text((x_pos, pos_y), line, font=font, fill=(255, 255, 255))
            pos_y += u_height + pad
        return pos_y

    if upper_text:
        current_h = draw_text_wrapped(draw, upper_text, width=15, font=m_font, pos_y=current_h)

    if lower_text:
        draw_text_wrapped(draw, lower_text, width=15, font=m_font, pos_y=i_height - int((20 / 640) * i_width) - font.getsize(lower_text)[1])

    image_name = "memify.webp"
    webp_file = os.path.join(image_name)

    try:
        img.save(webp_file, "webp")
    except Exception as e:
        raise Exception(f"Error saving image: {e}")

    return webp_file
