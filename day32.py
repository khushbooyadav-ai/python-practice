class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, item, amount):
        self.expenses.append(Expense(item, amount))

    def total(self):
        total = 0
        for e in self.expenses:
            total = total + e.amount
        return total

    def find(self, item):
        for e in self.expenses:
            if e.item == item:
                return e
        return None

    def delete(self, item):
        e = self.find(item)
        if e is None:
            raise ValueError("no such expense.")
        self.expenses.remove(e)