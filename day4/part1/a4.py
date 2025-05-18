class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        return self.brand, self.model
    
car1 = Car('Toyota','Corolla')

print(car1.display())