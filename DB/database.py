import sqlite3 as sq

with sq.connect("jokes.sqlite") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE jokes (
    id INTEGER PRIMARY KEY UNIQUE,
    text_field TEXT NOT NULL UNIQUE ,
    likes      INTEGER,
    dislikes   INTEGER
    )""")


