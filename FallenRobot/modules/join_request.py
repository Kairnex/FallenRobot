import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ChatJoinRequestHandler

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

WELCOME_MESSAGE = "Hi {name}! 👋 Welcome to the group."

def accept_join_request(update: Update, context: CallbackContext):
    """Accepts a user's join request and sends them a welcome message."""
    try:
        chat_id = update.effective_chat.id
        user = update.effective_user

        if user:
            first_name = user.first_name or "User"
            context.bot.approve_chat_join_request(chat_id, user.id)
            logging.info(f"✅ Accepted join request from {first_name} in chat {chat_id}")

            # Send a private welcome message
            context.bot.send_message(chat_id=user.id, text=WELCOME_MESSAGE.format(name=first_name))

    except Exception as e:
        logging.error(f"❌ Error in accept_join_request: {e}", exc_info=True)

def main():
    """Start the bot and register the handler."""
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Use ChatJoinRequestHandler instead of MessageHandler
    dp.add_handler(ChatJoinRequestHandler(accept_join_request))

    logging.info("✅ Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
