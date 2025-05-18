class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year


car = Car('Honda','Civic',2022)
print(car.make)
print(car.model)
print(car.year)