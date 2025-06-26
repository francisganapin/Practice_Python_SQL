import os

if os.path.exists('data.txt'):
    with open("data.txt",'r') as file:
        print(file.read())
else:
    print("File does not exist")