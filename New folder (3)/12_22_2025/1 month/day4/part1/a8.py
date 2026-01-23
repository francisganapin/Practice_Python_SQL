class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount('Alice',1000)
print(account._BankAccount__balance)  