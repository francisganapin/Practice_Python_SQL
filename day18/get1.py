import json


with open('config.json','r') as f:
    config = json.load(f)

print("App version:",config.get('version','1.0.0'))