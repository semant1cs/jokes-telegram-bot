import sqlite3 as sq


def delete_database_table(database_name):
    cur.execute(f'DROP TABLE {database_name}')


with sq.connect("jokes.sqlite") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS jokes (
    id INTEGER PRIMARY KEY UNIQUE,
    text_field TEXT NOT NULL UNIQUE ,
    likes      INTEGER,
    dislikes   INTEGER
    )""")

    delete_database_table("jokes")





