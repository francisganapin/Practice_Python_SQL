user_input = input('Enter your age: ')

if user_input.isdigit():
    age = int(user_input)
    print('You are',age,'years old.')
else:
    print(f"{user_input} invalid input.please enter digit only")