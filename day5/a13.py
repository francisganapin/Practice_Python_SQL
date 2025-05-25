from collections import defaultdict

grouped = defaultdict(list)

data = [('fruint','apple'),('fruit','banana'),('veg','carrot')]

for key, value in data:
    grouped[key].append(value)

print(grouped)