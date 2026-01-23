import sqlite3

name = input('Enter your name: ')
age = input('Enter your age:   ')



conn = sqlite3.connect('example.db')
cursor = conn.cursor()


cursor.execute('INSERT INTO user (name,age) VALUES (?,?)',(name,int(age)))

conn.commit()
conn.close()

print(f'{name} & {age} was successfully added to your Users')