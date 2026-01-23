emails = {
    'alice':'alice@example.come',
    'bob':'bob@spam.com',
    'carol':'carol@example.com'
}


trusted_users = [user for user,email in emails.items() if email.endswith('@example.com')]

print(trusted_users)