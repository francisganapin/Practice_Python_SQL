def validate_password(password):
    if 8 <= len(password) <= 16:
        return "Valid Lenght"
    return "Password too short or too Long"