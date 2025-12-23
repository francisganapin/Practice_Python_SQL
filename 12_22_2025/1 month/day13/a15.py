users = {
    101: 'active',
    102: 'inactive',
    103: 'active'
}

num_active = len([1 for _, status in users.items() if status == 'active'])

print(num_active)