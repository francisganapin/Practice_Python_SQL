class Dog:
    def __init__(self,name):
        self.name = name
    
    def bark(self):
        print(self.name,'says aso')


d = Dog('Browny')
d.bark()