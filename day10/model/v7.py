try:
    with open("data.txt",'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not Found")