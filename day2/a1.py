student ={
    'name':'John',
    'age':20,
    'grade':'A'
}

print(student['name'])

student['age'] = 21
student['major'] = 'Math'

print(student['age'])
print(student['major'])


if 'name' in student:
    print('Name exists')