loggedIn = True
isAdmin = True


if loggedIn:
    if isAdmin:
        print('Welcome Admin')
    else:
        print('Welcome,User')
else:
    print('Please log In')