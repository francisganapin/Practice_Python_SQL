import requests


res = requests.get('https://api.restful-api.dev/objects')
print(res.json())