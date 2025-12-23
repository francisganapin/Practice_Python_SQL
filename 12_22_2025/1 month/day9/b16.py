class PassWordTooShortError(Exception):
    pass


password  = input("Enter password: ")

if len(password) < 6:
    raise PassWordTooShortError("X password")
else:
    print("Password accepted")