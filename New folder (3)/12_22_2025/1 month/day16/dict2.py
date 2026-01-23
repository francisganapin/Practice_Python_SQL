

car = {'brand':'toyota','model':'vios','year':2000}


for key in car:
    print(key)

for value in car.values():
    print(value)

for key,value in car.items():
    print(f'{key}: {value}')