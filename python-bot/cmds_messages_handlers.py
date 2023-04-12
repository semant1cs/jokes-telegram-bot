from telegram import ReplyKeyboardRemove

from database import get_random_joke_from_db, update_joke_read
from keyboard import start_keyboard, choose_theme_joke_keyboard, messages_to_handle_keyboard, removed_keyboard


async def send_joke(update, context):
    added_joke = get_random_joke_from_db(update.effective_chat.id)

    if added_joke.count_jokes_after == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Доступных анекдотов не осталось\nПриходите позже:)",
                                       reply_markup=removed_keyboard)
        ReplyKeyboardRemove.remove_keyboard()
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=added_joke.text_joke)
        update_joke_read(added_joke.id, update.effective_chat.id)


async def handle_start_command(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет, это бот, который отправляет анекдоты, придуманные искусственным интеллектом",
        reply_markup=start_keyboard
    )

async def start_dialog(update, context):
    added_joke = get_random_joke_from_db(update.effective_chat.id)

    if added_joke.count_jokes_after == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Доступных анекдотов не осталось\nПриходите позже:)",
                                       reply_markup=removed_keyboard)
    else:
        await send_joke(update,context)


async def reply_to_feedback(update, context):
    added_joke = get_random_joke_from_db(update.effective_chat.id)

    if added_joke.count_jokes_after == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Доступных анекдотов не осталось\nПриходите позже:)",
                                       reply_markup=removed_keyboard)

    else:
        if update.message.text == "👍":
            await send_joke(update, context)
            # набор инструкций для лайка


        elif update.message.text == "👎":
            await send_joke(update, context)
            pass
            # набор инструкций для дизлайка
        # То есть мы в БД, в поле likes, dislikes инкрементируем значение записи таблицы


async def reply_to_unknown_message(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Не могу распознать ваше сообщение. Я генерирую анекдот только после получения его оценки при помощи эмодзи 👍 или 👎"
    )


async def get_help(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Этот бот отправляет анекдоты, сгенерированные искусственным интелектом\nВы получаете следующий анекдот"
             " после отправки оценки (нравится/не нравится)\nНа следующий день в телеграмм канал будут выложены "
             "самые популярные анекдоты прошлого дня\n"
    )
    await context.bot.send_photo(photo="https://basket-09.wb.ru/vol1181/part118162/118162658/images/c516x688/1.jpg",
                                 chat_id=update.effective_chat.id)
