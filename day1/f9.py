import sqlite3


def get_integer_input(prompt):
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError:
            print('Please enter valind input Number for AGE')

def get_letter_input(prompt):
    while True:
        name = input(prompt)
        if name.isalpha(): 
                return name
        else:
            print('Please enter a letter withou number for Name')


name = get_letter_input('Enter your name: ')
age = get_integer_input('Enter your age:  ')

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO user (name,age) Values(?,?)',(name,int(age)))

conn.commit()
conn.close()

print(f'{name} & {age} was successfully added to your Users')