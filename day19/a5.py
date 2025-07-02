users = {
    'username':'admin',
    'password':'1234',
    '2fa':None
}


if all (users.values()):
    print('login success')
else:
    missing = [k for k,v in users.items() if not v]
    print(f'Login failed:Missing {','.join(missing)}')