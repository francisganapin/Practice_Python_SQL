def has_permision(role,action):
    permissions = {
        "admin":['view',"add",'delete','edit'],
        'editor':['view','edit'],
        'viewer':['view']
    }
    return action in permissions.get(role,[])

if has_permision('editor','view'):
    print("Access granted")
else:
    print("Access denied")