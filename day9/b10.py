admin = ["admin","admin2"]
staff = ['staff1','staff2']
guest = ['guest1','guest2']


username = input("Enter your username: ")

if username in admin:
    print("Hello Admin! You have full Access")
elif username in staff:
    print("Hello Staff! You have medium Access")
elif username in guest:
    print("Hello Guest! you have limited access")
else:
    print("User not recognized")