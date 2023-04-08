from models import *

with db:
    db.create_tables([Joke, JokeRead])

print('done')
