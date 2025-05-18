class Circle:
    def __init__(self,r):
        self.r =r

    def area(self):
        a = 3.13 * self.r ** 2
        return a
    
ins = Circle(5)

print('Area of the circle:',ins.area())