

def get_integer_input(prompt):
    try:
        value = int(input(prompt))

        return value
    except ValueError:
        print('Error invalid input')

n = get_integer_input('Input and Integer: ')

print('Input value:',n)