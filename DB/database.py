import sqlite3 as sq


def delete_database_table(database_name):
    cur.execute(f'DROP TABLE {database_name}')


with sq.connect("jokes.sqlite") as con:
    cur = con.cursor()

    delete_database_table('jokes')

    cur.execute("""CREATE TABLE IF NOT EXISTS jokes (
    text_field TEXT NOT NULL UNIQUE ,
    likes      INTEGER NOT NULL DEFAULT 0,
    dislikes   INTEGER NOT NULL DEFAULT 0
    )""")








