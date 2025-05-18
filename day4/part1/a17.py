from collections import namedtuple

Person = namedtuple('Person',['name','age'])
p1 = Person('Ana',25)

print(p1.name)
print(p1.age)