import logging
from dotenv import load_dotenv
import os

from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from cmds_messages_handlers import start_dialog, reply_to_unknown_message, reply_to_feedback, get_help
from keyboard import messages_to_handle_keyboard_buttons

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('API_TOKEN')).build()


    start_handler = CommandHandler('start', start_dialog)
    help_handler = CommandHandler('help', get_help)
    feedback_handler = MessageHandler(filters.Text(messages_to_handle_keyboard_buttons), reply_to_feedback)
    unknown_message_handler = MessageHandler(filters.TEXT & ~filters.Text(messages_to_handle_keyboard_buttons), reply_to_unknown_message)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(unknown_message_handler)
    application.add_handler(feedback_handler)

    application.run_polling()
