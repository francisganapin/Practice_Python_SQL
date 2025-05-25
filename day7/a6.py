class Person:
    def greet(self):
        print('Hello from Person')

class Emp(Person):
    def greet(self):
        print('Hello from Emp')

e = Emp()
e.greet()