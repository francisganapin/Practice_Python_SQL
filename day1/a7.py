import sqlite3
conn = sqlite3.connect('test.db')


conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             ADDRESS  CHAR(50),
             SALARY REAL);
             
             ''')

conn.close()