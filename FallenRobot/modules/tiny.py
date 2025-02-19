import os
import cv2
from PIL import Image
from FallenRobot import telethn as tbot
from FallenRobot.events import register
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

# Initialize the bot
app = Client("FallenRobot", api_id=9696783, api_hash="3e74a9830493e9261410a947428dbb34", bot_token="7944268865:AAHX3D4Z-3mod4jNXJxBdNNsScFAmIeZHVA")

WELCOME_MESSAGE = "Hi {name}! 👋 Welcome to the group. Feel free to participate and enjoy your time here!"

@app.on_chat_join_request()
async def accept_join_request(client: Client, chat_request: ChatJoinRequest):
    try:
        await client.approve_chat_join_request(chat_request.chat.id, chat_request.from_user.id)
        print(f"Accepted join request from {chat_request.from_user.first_name} in {chat_request.chat.title}")
        
        await client.send_message(
            chat_id=chat_request.from_user.id,
            text=WELCOME_MESSAGE.format(name=chat_request.from_user.first_name or "User")
        )
    except Exception as e:
        print(f"Failed to accept join request or send welcome message: {e}")

@app.on_message(filters.command("broadcast") & filters.user(6999372290))  
async def broadcast_message(client: Client, message):
    if len(message.command) < 2:
        await message.reply("Usage: /broadcast [message]")
        return

    broadcast_text = message.text.split(" ", 1)[1]
    chat_id = message.chat.id

    try:
        async for member in client.get_chat_members(chat_id):
            try:
                if not member.user.is_bot:
                    await client.send_message(chat_id=member.user.id, text=broadcast_text)
                    print(f"Sent broadcast to {member.user.first_name}")
            except Exception as e:
                print(f"Failed to send message to {member.user.first_name}: {e}")
        await message.reply("Broadcast completed!")
    except Exception as e:
        await message.reply(f"Failed to broadcast: {e}")

@register(pattern="^/tiny ?(.*)")
async def _(event):
    reply = await event.get_reply_message()
    if not (reply and reply.media):
        await event.reply("`Please reply to a sticker`")
        return
    
    kontol = await event.reply("`Processing tiny...`")
    ik = await tbot.download_media(reply)
    im1 = Image.open("FallenRobot/resources/blank_background.png")
    
    if ik.endswith(".tgs"):
        await tbot.download_media(reply, "blank_background.tgs")
        os.system("lottie_convert.py blank_background.tgs json.json")
        with open("json.json", "r") as json_file:
            jsn = json_file.read().replace("512", "2000")
        with open("json.json", "w") as json_file:
            json_file.write(jsn)
        os.system("lottie_convert.py json.json blank_background.tgs")
        file = "blank_background.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        success, busy = iik.read()
        if success:
            cv2.imwrite("i.png", busy)
            fil = "i.png"
            im = Image.open(fil)
            z, d = im.size
            xxx, yyy = (200, 200) if z == d else (200 + 5 * ((z / (z + d)) * 100 - 50), 200 + 5 * ((d / (z + d)) * 100 - 50))
            k = im.resize((int(xxx), int(yyy)))
            k.save("k.png", format="PNG", optimize=True)
            im2 = Image.open("k.png")
            back_im = im1.copy()
            back_im.paste(im2, (150, 0))
            back_im.save("o.webp", "WEBP", quality=95)
            file = "o.webp"
            os.remove(fil)
            os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        xxx, yyy = (200, 200) if z == d else (200 + 5 * ((z / (z + d)) * 100 - 50), 200 + 5 * ((d / (z + d)) * 100 - 50))
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    
    await tbot.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await kontol.delete()
    os.remove(file)
    os.remove(ik)

# Start the bot
app.run()

__mod_name__ = "Tɪɴʏ"
__help__ = """
❍ /tiny*:* reply a sticker and see magic
"""
