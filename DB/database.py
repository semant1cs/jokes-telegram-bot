import sqlite3

try:
    conn = sqlite3.connect("jokes.sqlite")
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO `jokes` (textField, likes, dislikes) VALUES (?, ?, ?)", (1000,))

    users = cursor.execute("SELECT * FROM `jokes`")
    print(users.fetchall())

    conn.commit()

except sqlite3.Error as error:
    print("Error", error)

finally:
    if conn:
        conn.close()
