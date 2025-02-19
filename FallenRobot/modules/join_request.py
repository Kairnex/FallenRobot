from telegram import Update, ChatMemberUpdated
from telegram.ext import ChatMemberHandler, CallbackContext, Updater

import logging


WELCOME_MESSAGE = "Hi {name}! 👋 Welcome to the group. Feel free to participate and enjoy your time here!"


def accept_join_request(update: Update, context: CallbackContext):
    try:
        chat_id = update.effective_chat.id
        user = update.effective_user
        first_name = user.first_name or "User"

        if update.chat_member.new_chat_member.status == "member":  
            context.bot.send_message(chat_id=user.id, text=WELCOME_MESSAGE.format(name=first_name))
            logging.info(f"Accepted join request from {first_name} in chat {chat_id}")

    except Exception as e:
        logging.error(f"Failed to accept join request: {e}")

join_request_handler = ChatMemberHandler(accept_join_request, ChatMemberHandler.CHAT_MEMBER)

