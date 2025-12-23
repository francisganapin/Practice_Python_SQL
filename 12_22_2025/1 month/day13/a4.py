users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


for user,status in users.copy().items():
    if status == 'inactive':
        del users[user]


active_users = {}

for user,status in users.items():
    if status == 'active':
        active_users[user] = status

    
print('Remain users:',users)
print('Active users only:',active_users)