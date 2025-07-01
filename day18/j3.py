import json



bad_json = '{"name":"alex","age":25 }'


try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print('Error decoding json:',e)

print(data)