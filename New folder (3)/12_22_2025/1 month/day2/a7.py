d = {"a":1,"b":2,"c":3}

value_to_find = 2

key = next((k for k,v in d.items() if v == value_to_find),None)
print(key)