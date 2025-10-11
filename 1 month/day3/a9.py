def dynamic_cast(value,to_type):
    try:
        return to_type(value)
    except(ValueError,TypeError):
        return None
    
print(dynamic_cast('123',int))
print(dynamic_cast('abc',int))