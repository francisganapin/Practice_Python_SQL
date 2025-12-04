import requests

url = 'https://api.restful-api.dev/objects'
items = requests.get(url).json()


for item in items:
    data = item.get('data')
    if data and 'price' in data:
        print(item['name'],data['price'])