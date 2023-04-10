from peewee import *

db = SqliteDatabase('jokes.sqlite')


class BaseModel(Model):
    class Meta:
        database = db
        order_by = 'joke_id'


class Joke(BaseModel):
    joke_id = PrimaryKeyField(unique=True)
    text_field = TextField()
    likes = IntegerField()
    dislikes = IntegerField()
    rating = IntegerField()

    class Meta:
        db_table = 'jokes'


class JokeRead(BaseModel):
    joke_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        db_table = 'jokes_read'
