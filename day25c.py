class Wallet:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def spend(self, amount):
        if amount>self.balance:
            raise ValueError("not enough money.")
        self.balance = self.balance-amount

w = Wallet(100)
w.deposit(50)
w.spend(30)
assert w.balance == 120
try:
    w.spend(500)
    assert False, "should have raised ValueError"
except ValueError:
    pass
assert w.balance == 120
print("all checks passed")