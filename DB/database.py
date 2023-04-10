from models import *
from mock_data import *
import random


def get_random_joke(count_jokes):
    return random.randint(1, count_jokes)

def get_random_joke_from_db():
    with db:
        id_joke = get_random_joke(len(Joke))

        joke = Joke.select().where(Joke.joke_id == id_joke)

        for text in joke:
            return text.text_field


print('done')
