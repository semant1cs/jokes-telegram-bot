from models import *
from mock_data import *

with db:
    # единичное создание записи в таблице
    Joke.create(text_field='uaua', likes=14, dislikes=2, rating=13)


    # множественное создание записей из моков
    Joke.insert_many(insert_jokes).execute()

print('done')
