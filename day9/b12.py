users = {
    "admin":{"password":"admin123","role":"admin"},
    "staff":{"password":"staffpass","role":"staff"},
    "guest1":{"password":"guestpass","role":"guest"}
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users:
    if password == users[username]['password']:
        role = users[username]['role']
    
        if role == 'admin':
            print("Welcome admin! you have full access")
        elif role == 'staff':
            print("Welcome staff! you can view and edit some")
        elif role == "guest":
            print("Welcome guest read-only access granted")
    else:
        print("X incorect password")
else:
    print("X User not found")