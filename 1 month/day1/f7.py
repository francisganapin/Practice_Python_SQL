def get_invalid_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print('Error input should letters not numbers')

name = get_invalid_name('Enter your name: ')

print('Hello',name)