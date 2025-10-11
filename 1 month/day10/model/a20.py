search = input("Enter name to seach:")

with open("data.txt","r") as file:
    names = file.read().splitlines()

if search in names:
    print("Found",search)
else:
    print("X Not Found.")