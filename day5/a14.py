actions = []

actions.append(lambda:print('Hello'))
actions.append(lambda:print('World'))


for action in actions:
    action()