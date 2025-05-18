from collections import defaultdict


inventory = defaultdict(int)

inventory['apple'] += 1
inventory['banana'] += 1
inventory['apple'] += 1


print(inventory)
