

import requests
response = requests.get('https://simple-books-api.glitch.me/status')

data_json = response.json()






data  = { 'status':data_json['status'] }
print(data)