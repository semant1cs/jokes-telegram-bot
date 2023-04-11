import random

from models import *


class AddedJoke:
    def __init__(self, id, text_joke):
        self.id = id
        self.text_joke = text_joke


def get_random_joke_id_from_list(list):
    if len(list) != 0:
        return list[random.randint(0, len(list) - 1)]
    return -1


def get_random_joke_from_db(user_id):
    with db:
        unread_jokes = get_unread_jokes(user_id)
        random_joke_id = get_random_joke_id_from_list(unread_jokes)

        if random_joke_id == -1:
            return AddedJoke(0, 0)

        available_jokes = Joke.select().where(Joke.joke_id == random_joke_id)

        for text in available_jokes:
            return AddedJoke(random_joke_id, text.text_field)


def update_joke_read(joke_id, user_id):
    with db:
        JokeRead.insert(joke_id=joke_id, user_id=user_id).execute()


def get_unread_jokes(user_id):
    with db:
        read_jokes = []
        all_jokes = []

        query_all_jokes = Joke.select()
        query_read_jokes = JokeRead.select().where(JokeRead.user_id == user_id)

        for joke in query_all_jokes:
            all_jokes.append(joke.joke_id)

        for joke in query_read_jokes:
            read_jokes.append(joke.joke_id)

        for joke in read_jokes:
            if joke in all_jokes:
                all_jokes.remove(joke)

        return all_jokes


# Добавление анекдотов в БД
# Joke.insert_many(insert_jokes).execute()

print(get_random_joke_from_db(854998259))

print('done')
