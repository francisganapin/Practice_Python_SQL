import json
import requests


response = requests.get('https://jsonplaceholder.typicode.com/users')
users = json.loads(response.text)

print(users[1]['name'])