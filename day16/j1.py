import json


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.load(x)

# the result is a Python dictionary:
print(y["age"])