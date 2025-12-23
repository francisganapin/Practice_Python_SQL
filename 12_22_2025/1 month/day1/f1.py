import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age integer NOT NULL
    )
''')

conn.commit()