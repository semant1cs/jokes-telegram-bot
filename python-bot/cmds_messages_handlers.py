from keyboard import keyboard_markup


async def start_dialog(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет, это бот, который отправляет анекдоты, придуманные искусственным интеллектом",
        reply_markup=keyboard_markup
    )


async def reply_to_feedback(update, context):
    if update.message.text == "👍":
        pass
        # набор инструкций для лайка
    elif update.message.text == "👎":
        pass
        # набор инструкций для дизлайка
    # То есть мы в БД, в поле likes, dislikes инкрементируем значение записи таблицы

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Ваша оценка: {update.message.text} учтена! \nСпасибо.'
    )


async def reply_to_unknown_message(update, context):


    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Не могу распознать ваше сообщение. Я генерирую анекдот только после получения его оценки при помощи эмодзи 👍 или 👎"
    )

