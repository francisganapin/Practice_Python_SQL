import json

json_string = '{"name":"jane","age":22}'

python_data = json.loads(json_string)

print(python_data['name'])


back_to_json = json.dumps(python_data)