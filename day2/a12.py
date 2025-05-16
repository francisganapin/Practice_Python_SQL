students = [
    {'name':'John','class':'Math'},
    {'name':'Alice','class':'Science'},
    {'name':'Bob','class':'Math'}
]

class_group = {}

for student in students:
    class_name = student['class']
    if class_name not in class_group:
        class_group[class_name] = []
    class_group[class_name].append(student['name'])

print(class_group)