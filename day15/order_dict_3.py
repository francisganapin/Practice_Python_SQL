from collections import OrderedDict

cache = OrderedDict()
cache['a'] = 1
cache['b'] = 2
cache['c'] = 3

cache.move_to_end('a')

cache.popitem(last=False)
print(cache)