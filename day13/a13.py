users = {
    'jane':'verified',
    'mark':'unverified',
    'lucas':'verified'
}

verified_list = [f'@{users}' for user,status in users.items() if status == 'verified']

print(verified_list)