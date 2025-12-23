class MyInt:
    def __index__(self):
        return 5


x = MyInt()
print(bin(x))
print([0,1,2,3,4,5,6,7][x])