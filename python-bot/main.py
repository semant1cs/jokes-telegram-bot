import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters


API_token = "5878332892:AAF1xsTx7NcmWnKb5xwCMTdcRa2y-qIb4Iw"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def reply_to_feedback(update, context):
    await context.bot.send_message(chat_id= update.effective_chat.id, text=f'Ваша оценка: {update.message.text} учтена! Спасибо.')


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_token).build()

    start_handler = CommandHandler('start', start)
    feedback_handler = MessageHandler(filters.TEXT, reply_to_feedback)

    application.add_handler(feedback_handler)
    application.add_handler(start_handler)

    application.run_polling()
