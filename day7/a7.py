class A:
    def feature(self):
        print('Feature from A')

class B:
    def feature(self):
        print('Feature from B')

class C(A,B):
    pass

c = C()
c.feature()