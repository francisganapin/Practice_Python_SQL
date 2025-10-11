username = input("Enter your name: ")

if username.isalpha() and len(username) >= 3:
    print("Username accepted")
else:
    print("Username must have only letters and 3 characters")