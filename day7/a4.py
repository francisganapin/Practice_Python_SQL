class Person(object):

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def Display(self):
        print(self.name,self.id)

emp = Person('Satyam',102)

emp.Display()


class Emp(Person):

    def Print(self):
        print('Emp class Called')

Emp_details = Emp('Mayank',103)

Emp_details.Display()

Emp_details.Print()