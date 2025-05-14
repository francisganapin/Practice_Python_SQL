def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('invalid input')

n = get_integer_input('Input a integer: ')


print('Input a value:', n)