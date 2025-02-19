from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, filters

import logging

def accept_join_request(update: Update, context: CallbackContext):
    try:
        chat_id = update.effective_chat.id
        user = update.effective_user
        first_name = user.first_name or "User"

        context.bot.approve_chat_join_request(chat_id, user.id)
        logging.info(f"✅ Accepted join request from {first_name} in chat {chat_id}")

        context.bot.send_message(chat_id=user.id, text=f"Hi {first_name}! 👋 Welcome to the group.")

    except Exception as e:
        logging.error(f"❌ Failed to accept join request: {e}")


join_request_handler = MessageHandler(filters.StatusUpdate.JOIN_REQUEST, accept_join_request)
