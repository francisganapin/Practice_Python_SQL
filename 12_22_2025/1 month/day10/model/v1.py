try:
    age = int(input("Enter your age: "))
    print("your entered age:",age)
except ValueError:
    print("Please enter a valid number.")