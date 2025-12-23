class Person:
    def __init__(self,name):
        self.name = name

people = []
people.append(Person('Alice'))
people.append(Person('Bob'))

for p in people:
    print(p.name)