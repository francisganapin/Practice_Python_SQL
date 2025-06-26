user_input = input("Enter your age: ")

try:
    age = int(user_input)
    if age < 0:
        raise ValueError("X age cannot be negative")
    print(f"your age is {age}")
except ValueError as ve:
    print ("Vallue error occured",ve)