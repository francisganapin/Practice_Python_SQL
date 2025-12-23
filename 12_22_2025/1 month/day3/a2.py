class Item:
    def __init__(self,price):
        self.price = price
    
    def __int__(self):
        return int(self.price)
    
    def __float__(self):
        return float(self.price)
    
    def __str__(self):
        return f"${self.price}"
    

item = Item(29.99)

print(int(item))
print(float(item))
print(str(item))