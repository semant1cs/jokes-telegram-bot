from models import *
import random
from mock_data import *


class AddedJoke:
    def __init__(self, id, text_joke):
        self.id = id
        self.text_joke = text_joke


def get_random_joke(count_jokes):
    return random.randint(1, count_jokes)


def get_random_joke_from_db():
    with db:
        id_joke = get_random_joke(len(Joke))

        joke = Joke.select().where(Joke.joke_id == id_joke)

        for text in joke:
            return AddedJoke(id_joke, text.text_field)


def update_joke_read(joke_id, user_id):
    with db:
        jokeReads = JokeRead.insert(joke_id=joke_id, user_id=user_id).execute


# Добавление анекдотов в БД
# Joke.insert_many(insert_jokes).execute()


print('done')
