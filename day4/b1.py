from collections import ChainMap

dict1 = {"a":1,'b':2}
dict2 = {'b':3,'c':4}

combined = ChainMap(dict1,dict2)

print(combined['b'])
print(combined['c'])