import requests


response = requests.get('https://simple-books-api.glitch.me/books')
data__json = response.json()

id_ = []
name = []
type_ = []
available = []

for i in data__json:
    id_.append(i['id'])
    name.append(i['name'])
    type_.append(i['type'])
    available.append(i['available'])

data = {'id':id_,'name':name,'type':type_,'available':available}

print(data)