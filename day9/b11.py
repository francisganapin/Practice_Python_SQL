users = {
    'admin':"admin123",
    "staff":"staffpass",
    "guest1":'guestpass'
}

username = input("Enter your username: ")
password = input("Enter your password: ")


if username in users:
    if password == users[username]:
        print(f"Welcome, {username}!")
    else:
        print("x Incorrect password.")
else:
    print("X username not found.")