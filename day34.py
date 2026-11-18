import json

class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, item, amount):
        self.expenses.append(Expense(item, amount))

    def save(self, path):
        data = []
        for e in self.expenses:
            data.append({"item": e.item, "amount": e.amount})
        with open(path, "w") as f:
            json.dump(data, f)

    def load(self, path):
        try:
            with open(path) as f:
                data = json.load(f)
        except FileNotFoundError:
            self.expenses = []
            return
        self.expenses = []
        for d in data:
            self.add(d["item"], d["amount"])
