import json

with open('config.json') as f:
    config = json.load(f)


if config['debug'] == 'true':
    print('Debug mode is On')
else:
    print('Debug mode is Off')


print('Database host:',config['database']['host'])