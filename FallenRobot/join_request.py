from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import logging

WELCOME_MESSAGE = "Hi {name}! 👋 Welcome to the group. Feel free to participate and enjoy your time here!"

def accept_join_request(update: Update, context: CallbackContext):
    try:
        chat_id = update.effective_chat.id
        user = update.effective_user
        first_name = user.first_name or "User"

        context.bot.approve_chat_join_request(chat_id, user.id)
        logging.info(f"Accepted join request from {first_name} in chat {chat_id}")

        context.bot.send_message(chat_id=user.id, text=WELCOME_MESSAGE.format(name=first_name))

    except Exception as e:
        logging.error(f"Failed to accept join request: {e}")

join_request_handler = CommandHandler("start", accept_join_request)
