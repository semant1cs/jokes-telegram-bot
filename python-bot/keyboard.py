from telegram import ReplyKeyboardMarkup

messages_to_handle = ['👍', '👎']

keyboard_markup = ReplyKeyboardMarkup.from_row(one_time_keyboard=False, resize_keyboard=True, button_row=messages_to_handle)

