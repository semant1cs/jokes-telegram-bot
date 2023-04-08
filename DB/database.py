import sqlite3 as sq
import mock_data


def delete_database_table(database_name):
    cur.execute(f'DROP TABLE {database_name}')


with sq.connect("jokes.sqlite") as con:
    cur = con.cursor()


    cur.execute("""CREATE TABLE IF NOT EXISTS jokes (
    joke_id INTEGER NOT NULL UNIQUE,
    text_field TEXT NOT NULL UNIQUE,
    likes      INTEGER NOT NULL DEFAULT 0,
    dislikes   INTEGER NOT NULL DEFAULT 0
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS jokes_read(
    user_id INTEGER NOT NULL,
    joke_id INTEGER NOT NULL
    )""")

    query = """INSERT INTO jokes(joke_id, text_field, likes, dislikes)
     VALUES (?,?,?,?); """

    cur.executemany(query, mock_data.insert_jokes)

    con.commit()
    print(cur.rowcount)
