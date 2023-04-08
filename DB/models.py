from peewee import *


db = SqliteDatabase('jokes.sqlite')

class Joke(Model):
    joke_id = PrimaryKeyField(unique=True)
    text_field = TextField()
    likes = IntegerField
    dislikes = IntegerField
    rating = IntegerField

class JokeRead(Model):
    joke_id = IntegerField
    user_id = IntegerField

