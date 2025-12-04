import requests

url = 'https://dog.ceo/api/breeds/list/all'

res = requests.get(url).json()

print(res)