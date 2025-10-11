correct_password = 'letmein'

while True:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("Access granted")
        break
    else:
        print("Try again")