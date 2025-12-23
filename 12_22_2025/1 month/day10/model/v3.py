roles = {
    "admin":['view',"add","delete","edit"],
    "edit":['view','edit'],
    'viewer':['view']
}

username = input("Enter your username:")
user_role = input("Enter your role (admin/editor/viewer): ").lower()
action = input("What do you want to do(view/add/delete/edit):").lower()


if user_role in roles:
    if action in roles[user_role]:
        print(f"{username} is allowed to {action}")
    else:
        print(f"{username} is not allowed to 'action'.")
else:
    print("Unknown role.")