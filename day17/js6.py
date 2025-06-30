import json

json_str = '{"name":"francis","age":25}'

data = json.loads(json_str)
print(data['name'])