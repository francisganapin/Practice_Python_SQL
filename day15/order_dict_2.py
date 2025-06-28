from collections import OrderedDict

ordered = OrderedDict()
ordered['banana'] = 3
ordered['apple'] = 4
ordered['orange'] = 2


for fruit,quantity in ordered.items():
    print(f'{fruit}: {quantity}')