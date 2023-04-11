from keyboard import keyboard_markup
from database import get_random_joke_from_db, update_joke_read


async def send_joke(update, context):
    added_joke = get_random_joke_from_db(update.effective_chat.id)

    if added_joke.text_joke == 0 and added_joke.id == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Доступных анекдотов не осталось. \nПриходите позже:)")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=added_joke.text_joke)
        update_joke_read(added_joke.id, update.effective_chat.id)


async def start_dialog(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет, это бот, который отправляет анекдоты, придуманные искусственным интеллектом",
        reply_markup=keyboard_markup
    )

    await send_joke(update, context)


async def reply_to_feedback(update, context):
    added_joke = get_random_joke_from_db(update.effective_chat.id)

    if added_joke.text_joke == 0 and added_joke.id == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Доступных анекдотов не осталось. \nПриходите позже:)")
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'Ваша оценка: {update.message.text} учтена! \nСпасибо.'
        )

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
