students = [
    {'name':'alice','score':85},
    {'name':'bob','score':62},
    {'name':'charlies','score':95}
]


above = [student['name'] for student in students if student['score'] >= 85]

print(above)