import logging

from aiogram import Bot, Dispatcher, executor, types

API_token = "5878332892:AAF1xsTx7NcmWnKb5xwCMTdcRa2y-qIb4Iw"

logging.basicConfig(level=logging.INFO)

bot = Bot(API_token)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Привет, я")


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)

