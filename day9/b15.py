age = int(input('Enter your age: '))

if age < 0:
    raise ValueError("X age Cannot be negative")
else:
    print("Invalid age",age)