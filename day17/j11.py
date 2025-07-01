import json


with open('config2.json','r') as file:
    config = json.load(file)


print("App Name",config['app_name'])
print('Debug Mode',config['debug'])


db_config = config['database']
print("Connecting to DB:",db_config['host'],"on port",db_config['port'])


print('Enable Features:')
for feature in config['features']:
    print("-",feature)