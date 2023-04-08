import sqlite3
import sqlite3 as sq
import mock_data
from models import *


# def delete_database_table(database_name):
#     cur.execute(f'DROP TABLE {database_name}')
#
#
# with sq.connect("jokes.sqlite") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS jokes (
#     joke_id    INTEGER NOT NULL UNIQUE,
#     text_field TEXT NOT NULL UNIQUE,
#     likes      INTEGER NOT NULL DEFAULT 0,
#     dislikes   INTEGER NOT NULL DEFAULT 0,
#     rating     INTEGER NOT NULL DEFAULT 0
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS jokes_read(
#     user_id INTEGER NOT NULL,
#     joke_id INTEGER NOT NULL
#     )""")
#
#     # query = """INSERT INTO jokes(joke_id, text_field, likes, dislikes)
#     # VALUES (?,?,?,?); """
#
#     # cur.executemany(query, mock_data.insert_jokes)
#
#     con.commit()
#
# with sqlite3.connect('jokes.sqlite') as con:
#     cur = con.cursor()
#
#     query_count_rating = """UPDATE jokes SET rating = 100 * likes / (likes + dislikes)"""
#
#     cur.execute(query_count_rating)
#
#     query_output_data = """SELECT likes, dislikes, rating FROM jokes"""
#
#     cur.execute(query_output_data)
#
#     for i in cur:
#         print(i)

with db:
    db.create_tables([Joke, JokeRead])

print('done')
