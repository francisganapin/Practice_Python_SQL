user_input = input("Enter a note: ")

with open("c1.txt","a") as file:
    file.write(user_input + '\n')

print("Note saved")