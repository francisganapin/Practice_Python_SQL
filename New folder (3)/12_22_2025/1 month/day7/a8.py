class A:
    def feature(self):
        print('Feature from A')

class B:
    def feature(self):
        print('Feature from B')

class C(B,A):
    pass

c = C()
c.feature()
