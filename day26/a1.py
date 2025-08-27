error_counter = {}


while True:
    user_input = input('Enter error(or'exit' to end): ')

    if user_input.lower() == 'exit':
        break

    if user_input in error_counter:
        error_counter['user_input'] += 1
    else:
        error_counter[user_input] = 1

    print('Current Errors:',error_counter)

print('\nFinal Error Count:',error_counter)