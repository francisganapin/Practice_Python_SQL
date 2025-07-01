import json

with open('config.json','r') as f:
    config = json.load(f)

config['debug'] = False
print("New debug Value:",config['debug'])


with open('config.json','w') as f:
    json.dump(config,f,indent=4)