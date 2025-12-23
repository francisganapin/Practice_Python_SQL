import json


with open("config.json",'r') as f:
    config = json.load(f)


config['debug'] = False
print("New debug value:",config['debug'])