import random

from models import *


class AddedJoke:
    def __init__(self, id, text_joke):
        self.id = id
        self.text_joke = text_joke


def get_random_joke_id(count_jokes):
    return random.randint(1, count_jokes)


def get_random_joke_from_db():
    with db:
        id_joke = get_random_joke_id(len(Joke))

        joke = Joke.select().where(Joke.joke_id == id_joke)

        for text in joke:
            return AddedJoke(id_joke, text.text_field)


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

print(get_unread_jokes(854998259))


# Добавление анекдотов в БД
# Joke.insert_many(insert_jokes).execute()


print('done')
