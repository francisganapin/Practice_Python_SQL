user = {'role':'admin','is_active':True}

if user['role'] == 'admin' and user['is_active']:
    print('Grant full access')
else:
    print('Restricted access')