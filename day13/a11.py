users = {'Hans': 'active', 'Éléonore': 'active', '景太郎': 'active'}

active_users = [user for user,status in users.items() if status == 'active']

print(active_users)