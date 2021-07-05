class Bank:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,depot):
        self.depot=depot
        self.balance=self.balance+self.depot
        return 'New Balance:',self.balance

    def withdraw(self, draw):
        self.draw=draw
        self.balance=self.balance-draw
        return "New Balance:" ,self.balance

Balance=Bank(500)

print( Balance.deposit(200))
print( Balance.withdraw(300))
