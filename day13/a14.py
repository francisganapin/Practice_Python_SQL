users = {
    101:'active',
    102:'inactive',
    103:'active'
}

active_ids = [user_id for user_id,status in users.items() if status == 'active']

print(active_ids)