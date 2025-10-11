def multiplier(factor):
    return lambda x: x * factor

double = multiplier(2)
print(double(10))