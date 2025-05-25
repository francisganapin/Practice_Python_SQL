class Character:
    def attack(self):
        print('Basic attack')

class Warrior(Character):
    def attack(self):
        print('Sword Slash')
        super().attack()
    
class Mage(Character):
    def attack(self):
        print('Fireball')
        super().attack()

class Battlemage(Warrior,Mage):
    def attack(self):
        print('Battle strike!')
        super().attack()

bm = Battlemage()
bm.attack()