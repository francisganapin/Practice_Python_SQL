user = {"role":'admin','is_active':False}

if user['role'] == 'admin' and user['is_active']:
    print('grant full access')
else:
    print('Restricted access')