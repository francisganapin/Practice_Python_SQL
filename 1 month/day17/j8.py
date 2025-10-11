import requests
import json
from datetime import datetime



tests = [
    {
        'name':'Test Get User',
        'method':'Get',
        'url':'https://jsonplaceholder.typicode.com/users',
        'expected_status':200
    },
    {
        'name':'Test Create Post',
        'method':'POST',
        'url':"https://jsonplaceholder.typicode.com/posts",
        'body':{
            'title':"foo",
            'body':"bar",
            'userId':1
        },
        "expected_status":201
    }
]


results = []


for test in tests:
    method = test['method']
    url = test['url']
    headers = {'Content-Type':'application/json'}

    print(f"Running: {test['name']}")

    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url,json=test.get('body'),headers=headers)
        elif method == 'PUT':
            response = requests.put(url,json=test.get('body'),headers=headers)
        elif method == 'DELETE':
            respose = requests.delete(url)
        else:
            raise ValueError('Unsupported method')
        
        result = {
            'test_name':test['name'],
            'url':url,
            'status_code':response.status_code,
            'expected_status':test['expected_status'],
            'pass':response.status_code == test['expected_status'],
            'response':response.json()
        }

    except Exception as e:
        result = {
            'test_name':test['name'],
            'url':url,
            'error':str(e),
            'pass':False

        }
    result.append(result)

filename = f'api_test_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json'
with open(filename,'w') as f:
    json.dump(results,f,indent=4)

print(f'\nResults saved to: {filename}')