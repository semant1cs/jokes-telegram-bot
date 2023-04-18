import random

def decline_jokes(count_jokes):
    ones = count_jokes % 10
    tens = (count_jokes // 10) % 10

    if (tens == 0 or tens >= 2) and ones == 1:
        return 'анекдот доступен'
    elif 2 <= ones <= 4 and (tens == 0 or tens >= 2):
        return 'анекдота доступно'
    else:
        return 'анекдотов доступно'

def is_jokes_anymore(list_jokes):
    return list_jokes != 0

def get_random_joke_id_from_list(available_jokes):
    if len(available_jokes) != 0:
        return available_jokes[random.randint(0, len(available_jokes) - 1)]
    return -1
