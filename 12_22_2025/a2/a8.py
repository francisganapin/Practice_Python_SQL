people = [
    {'Name':'Francis',"age":25},
    {'Name':"Ana","age":30}
]

sorted_people = sorted(people,key=lambda x: x['age'])
print(sorted_people)