from telegram import ReplyKeyboardMarkup


messages_to_handle = ['👍', '👎']

keyboard_markup = ReplyKeyboardMarkup.from_column(messages_to_handle, one_time_keyboard=False, resize_keyboard=True)