from collections import ChainMap

original = {'x':10}
override = {'x':99}

cm = ChainMap(override,original)
print(cm['x'])