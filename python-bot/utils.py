def decline_jokes(count_jokes):
    ones = count_jokes % 10
    tens = (count_jokes // 10) % 10

    if (tens == 0 or tens >= 2) and ones == 1:
        return 'анекдот'
    elif 2 <= ones <= 4 and (tens == 0 or tens >= 2):
        return 'анекдота'
    else:
        return 'анекдотов'
