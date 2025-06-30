import json

users =[
    {'id':1,'name':'Francis'},
    {'id':2,'name':'Anna'},
    {'id':3,"name":'Mark'}
]


with open('user.json','w') as f:
    json.dump(users,f,indent=2)