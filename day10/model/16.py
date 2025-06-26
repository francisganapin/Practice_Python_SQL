phone = input("Enter your phone number: ")


if phone.isdigit() and len(phone) == 11:
    print("Phone number is accepted")
else:
    print("Invalid phone number. Must be 11 digit")