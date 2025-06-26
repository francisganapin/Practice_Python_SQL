try:
    raise ValueError("Something bad Happen")
except ValueError as e:
    print("Loggin errorz:",e)
    raise