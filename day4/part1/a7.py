class Protected:
    def __init__(self):
        self._age = 30

class Sublcass(Protected):
    def display_age(self):
        print(self._age)

obj = Sublcass()
obj.display_age()