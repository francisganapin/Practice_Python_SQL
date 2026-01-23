phone = input("Enter your phone number:")

if phone.startswith("63") and phone.isdigit() and len(phone) == 12:
    print('Valid phone number!')
else:
    print("Invalid phone number must start with '63' and be exactly 11 digit ")