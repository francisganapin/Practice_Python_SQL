import json


with open('data.json') as f:
    data = json.load(f)

with open('output.json','w') as f:
    json.dump(data,f,indent=4)