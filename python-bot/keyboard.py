from telegram import ReplyKeyboardMarkup


def construct_keyboard(buttons):
    return ReplyKeyboardMarkup.from_row(one_time_keyboard=False, resize_keyboard=True, button_row=buttons)


start_keyboard_buttons = ['Начать', '/help', 'О создателях']
choose_theme_joke_keyboard_buttons = ['Анекдоты на случайную тему']
messages_to_handle_keyboard_buttons = ['👍', '👎', '❌']
admin_keyboard_buttons = ['Начать', '/help', 'О создателях', 'Добавить анекдот']

start_keyboard = construct_keyboard(start_keyboard_buttons)
choose_theme_joke_keyboard = construct_keyboard(choose_theme_joke_keyboard_buttons)
messages_to_handle_keyboard = construct_keyboard(messages_to_handle_keyboard_buttons)
admin_keyboard = construct_keyboard(admin_keyboard_buttons)
