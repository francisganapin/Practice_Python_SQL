existing_users = ['admin','francis','maria']

while True:
    username = input("choose a username: ")
    if username in existing_users:
        print("Username already Taken.")
    else:
        print("Username Created")
        break