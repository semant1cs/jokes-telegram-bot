from peewee import *


db = SqliteDatabase('jokes.sqlite')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'joke_id'


class Joke(BaseModel):
    joke_id = IntegerField()
    text_field = TextField()
    likes = IntegerField()
    dislikes = IntegerField()
    rating = IntegerField()

    class Meta:
        db_table = 'text_field'

class JokeRead(BaseModel):
    joke_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        db_table = 'used_id'
