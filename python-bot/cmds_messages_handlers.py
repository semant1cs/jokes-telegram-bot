import telegram
import os
from dotenv import load_dotenv

from database import FeedbackJoke, AddedJoke, JokesStateClass
from keyboard import start_keyboard, choose_theme_joke_keyboard, messages_to_handle_keyboard, admin_keyboard
from utils import is_jokes_anymore

load_dotenv()


async def handle_start_command(update, context):
    if str(update.effective_chat.id) in os.getenv("ADMIN_IDS"):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Вы вошли в админ-панель",
            reply_markup=admin_keyboard
        )

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Привет, это бот, который отправляет анекдоты, придуманные искусственным интеллектом",
            reply_markup=start_keyboard
        )


async def start_dialog(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите тему анекдота",
                                   reply_markup=choose_theme_joke_keyboard)


async def get_help(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Этот бот отправляет анекдоты, сгенерированные искусственным интелектом\nВы получаете следующий анекдот"
             " после отправки оценки (нравится/не нравится)\nНа следующий день в телеграмм канал будут выложены "
             "самые популярные анекдоты прошлого дня\n"
    )


async def choose_theme_joke(update, context):
    added_joke = AddedJoke.get_random_joke_from_db(update.effective_chat.id)

    # Выбор темы анекдота

    if not is_jokes_anymore(added_joke.count_jokes_after):
        await send_no_available_jokes_message(update, context)
    else:
        await send_joke(update, context, messages_to_handle_keyboard)


async def print_about_us(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="@s3mant1cs \n@fishvel",
                                   parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)


async def send_joke(update, context, keyboard):
    added_joke = AddedJoke.get_random_joke_from_db(update.effective_chat.id)

    if not is_jokes_anymore(added_joke.count_jokes_after):
        await send_no_available_jokes_message(update, context)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=added_joke.text_joke,
                                       reply_markup=keyboard)
        FeedbackJoke.update_joke_read(added_joke.id, update.effective_chat.id)


async def send_no_available_jokes_message(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Доступных анекдотов не осталось\nПриходите позже:)",
                                   reply_markup=start_keyboard)


async def reply_to_feedback(update, context):
    if is_user_read_anyone_joke(update):
        last_read_joke = JokesStateClass.get_unread_jokes(update.effective_chat.id).read_jokes[-1]
    else:
        await handle_start_command(update, context)
        return

    if update.message.text == "👍":
        FeedbackJoke.increment_grade(last_read_joke, 'likes')
    elif update.message.text == "👎":
        FeedbackJoke.increment_grade(last_read_joke, 'dislikes')
    elif update.message.text == "❌":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Возвращайся ещё 🥺",
                                       reply_markup=start_keyboard)
        return
    await send_joke(update, context, messages_to_handle_keyboard)


async def reply_to_unknown_message(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Не могу распознать ваше сообщение. Я генерирую анекдот только после получения его оценки при помощи эмодзи 👍 или 👎"
    )


def is_user_read_anyone_joke(update):
    try:
        JokesStateClass.get_unread_jokes(update.effective_chat.id).read_jokes[-1]
    except IndexError:
        return False
    return True
