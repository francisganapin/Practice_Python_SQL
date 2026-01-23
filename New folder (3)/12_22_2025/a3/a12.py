import requests

url = 'https://api.restful-api.dev/objects'
items = requests.get(url).json()


max_item = None
max_price = 0

for item in items:
    data = item.get('data')
    if data and 'price' in data:
        if data['price'] > max_price:
            max_price = data['price']
            max_item = item

print('Most expensive',max_item['name'],max_price)