existing_numbers = ["63912345678", "63987654321", "63911223344"]


phone = input("Enter your phone number: ")

if phone.startswith('63') and phone.isdigit() and len(phone) == 12:
    print("Valid phone number")
elif phone in existing_numbers:
    print("Phone number already exist")
else:
    print("Phone number must start with 63 and be exactly 11 digit")