import logging
import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters

from cmds_messages_handlers import handle_start_command, start_dialog, reply_to_unknown_message, reply_to_feedback, \
    get_help, choose_theme_joke, print_about_us
from keyboard import messages_to_handle_keyboard_buttons, choose_theme_joke_keyboard_buttons

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    token_bot = os.getenv('API_TOKEN')
    application = ApplicationBuilder().token(token_bot).build()

    start_command_handler = CommandHandler('start', handle_start_command)
    start_dialog_handler = MessageHandler(filters.Text(['Начать']), start_dialog)
    about_us_handler = MessageHandler(filters.Text(['О создателях']), print_about_us)
    choose_theme_handler = MessageHandler(filters.Text(choose_theme_joke_keyboard_buttons), choose_theme_joke)
    help_handler = CommandHandler('help', get_help)
    feedback_handler = MessageHandler(filters.Text(messages_to_handle_keyboard_buttons), reply_to_feedback)
    unknown_message_handler = MessageHandler(filters.TEXT & ~filters.Text(messages_to_handle_keyboard_buttons),
                                             reply_to_unknown_message)

    all_handlers = [start_command_handler, start_dialog_handler, about_us_handler, choose_theme_handler, help_handler,
                    feedback_handler, unknown_message_handler]

    application.add_handlers(all_handlers)

    application.run_polling()
