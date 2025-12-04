import sqlite3


conn = sqlite3.connect('mydata.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age Integer NOT NULL,
    grade TEXT NOT NULL
    )
    
""")

conn.commit()
conn.close()
