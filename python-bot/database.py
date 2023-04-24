from models import *
from utils import get_random_joke_id_from_list
from mock_data import parse_jokes


class AddedJoke:
    def __init__(self, id, text_joke, count_jokes_after):
        self.id = id
        self.text_joke = text_joke
        self.count_jokes_after = count_jokes_after

    @staticmethod
    def get_random_joke_from_db(user_id):
        with db:
            unread_jokes = JokesStateClass.get_unread_jokes(user_id).unread_jokes
            random_joke_id = get_random_joke_id_from_list(unread_jokes)

            if random_joke_id == -1:
                return AddedJoke(0, 0, 0)

            available_jokes = Joke.select().where(Joke.joke_id == random_joke_id)

            for text in available_jokes:
                return AddedJoke(random_joke_id, text.text_field, len(unread_jokes))


class JokesStateClass:
    def __init__(self, unread_jokes, read_jokes):
        self.unread_jokes = unread_jokes
        self.read_jokes = read_jokes

    @staticmethod
    def get_unread_jokes(user_id):
        with db:
            unread_jokes = []
            read_jokes = []

            query_all_jokes = Joke.select()
            query_read_jokes = JokeRead.select().where(JokeRead.user_id == user_id)

            for joke in query_all_jokes:
                unread_jokes.append(joke.joke_id)

            for joke in query_read_jokes:
                read_jokes.append(joke.joke_id)
                if joke.joke_id in unread_jokes:
                    unread_jokes.remove(joke.joke_id)

            return JokesStateClass(unread_jokes, read_jokes)


class FeedbackJoke:
    def __init__(self, joke_id, likes, dislikes, rating):
        self.joke_id = joke_id
        self.likes = likes
        self.dislikes = dislikes
        self.rating = rating

    @staticmethod
    def update_joke_read(joke_id, user_id):
        with db:
            JokeRead.insert(joke_id=joke_id, user_id=user_id).execute()

    @staticmethod
    def increment_grade(joke_id, grade):
        with db:
            if grade == "likes":
                query_joke_to_grade = Joke.update(likes=Joke.likes + 1).where(Joke.joke_id == joke_id)
            elif grade == "dislikes":
                query_joke_to_grade = Joke.update(dislikes=Joke.dislikes + 1).where(Joke.joke_id == joke_id)
            query_joke_to_grade.execute()


# Добавление анекдотов в БД
def add_joke_from_other_source(url_jokes):
    jokes = parse_jokes(url_jokes)
    Joke.insert_many(jokes).execute()
    print('done')


def calculate_rating_jokes():
    with db:
        query_joke_rating_update = Joke.update(rating=100 * Joke.likes / (Joke.likes + Joke.dislikes))
        query_joke_rating_update.execute()


calculate_rating_jokes()
