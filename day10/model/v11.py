items = ['apple','banana','mango']

with open("data.txt",'w') as file:
    for item in items:
        file.write(item + "\n")