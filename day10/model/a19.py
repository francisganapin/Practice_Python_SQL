users = {
    "admin":"admin123",
    "francis":"loveCreatine",
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful. Welcome,",username + "!")
else:
    print("Invalid username or password")