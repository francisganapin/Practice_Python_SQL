def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier


double = make_multiplier(2)
print(double(5))