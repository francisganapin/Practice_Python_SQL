
person = {
    'name':'franics',
    'age':25,
    'city':'manila'
}

print('name',person['name'])
print('age',person['age'])


person['email'] = 'francis@example.com'


person['age'] = 26

del person['city']



for key, value in person.items():
    print(f'{key}: {value}')