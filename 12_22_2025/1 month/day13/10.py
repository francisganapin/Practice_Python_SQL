result = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(result)

active_users = [user for user,status in users.items() if status == 'active']