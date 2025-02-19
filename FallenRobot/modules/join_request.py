import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

WELCOME_MESSAGE = "Hi {name}! 👋 Welcome to the group."

def accept_join_request(update: Update, context: CallbackContext):
    try:
        chat_id = update.effective_chat.id
        user = update.effective_user

        if user:
            first_name = user.first_name or "User"
            context.bot.approve_chat_join_request(chat_id, user.id)
            logging.info(f"✅ Accepted join request from {first_name} in chat {chat_id}")

            context.bot.send_message(chat_id=user.id, text=WELCOME_MESSAGE.format(name=first_name))

    except Exception as e:
        logging.error(f"❌ Error in accept_join_request: {e}", exc_info=True)


join_request_handler = MessageHandler(Filters.status_update.chat_join_request, accept_join_request)

logging.info("✅ join_request module loaded successfully!")
