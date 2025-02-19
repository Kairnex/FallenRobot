import html

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram.utils.helpers import mention_html

import FallenRobot.modules.sql.approve_sql as sql
from FallenRobot import DRAGONS, dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler
from FallenRobot.modules.helper_funcs.chat_status import user_admin
from FallenRobot.modules.helper_funcs.extraction import extract_user
from FallenRobot.modules.log_channel import loggable



from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest






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
                if not member.user.is_bot:  # Skip bots
                    await client.send_message(chat_id=member.user.id, text=broadcast_text)
                    print(f"Sent broadcast to {member.user.first_name}")
            except Exception as e:
                print(f"Failed to send message to {member.user.first_name}: {e}")
        await message.reply("Broadcast completed!")
    except Exception as e:
        await message.reply(f"Failed to broadcast: {e}")
