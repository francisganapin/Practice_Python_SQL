import requests


response = requests.get('https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json')
data_json = response.json()

Name  = []
Price = []
Image = []
Type  = []


for i in data_json:
    Name.append(i['name'])
    Price.append(i['price'])
    Image.append(i['image'])
    Type.append(i['type'])

data = {'name':Name,'price':Price,'image':Image,'type':Type}
print(data)