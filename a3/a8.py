import requests

url = 'https://api.restful-api.dev/objects'
items = requests.get(url).json()


price = [item['data']['price'] for item in items
        if item.get('data') and 'price' in item['data']
]

print(price)