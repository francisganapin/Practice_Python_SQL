username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin123":
    print('Admin login successfull full granted.')
elif username != 'admin':
    print("Access denied you are not an admin")
else:
    print("Wrong password.Try again")