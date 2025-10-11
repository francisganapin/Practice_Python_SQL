class Person:
    def __init__(self,name):
        self.name = name
        print('Person init called')

class Emp(Person):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id
        print('Emp init called')

e = Emp('Alice',101)