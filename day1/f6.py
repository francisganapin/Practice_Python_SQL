import sqlite3

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('invalid Please input a number')
            



name = input('Enter your name: ')
age = get_integer_input('Input a age: ')



conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO user (name,age) Values(?,?)',(name,int(age)))

conn.commit()
conn.close()

print(f'{name} & {age} was successfully added to your Users')