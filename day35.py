import json

class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return f"{self.item}: {self.amount}"

class BudgetBook:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be positive.")
        self.limit = limit
        self.expenses = []

    def add(self, item, amount):
        if amount <= 0:
            raise ValueError("amount must be positive.")
        self.expenses.append(Expense(item, amount))

    def total(self):
        total = 0
        for e in self.expenses:
            total = total + e.amount
        return total

    def remaining(self):
        return self.limit - self.total()

    def over_budget(self):
        return self.total() > self.limit

    def biggest(self):
        if not self.expenses:
            return None
        return max(self.expenses, key=lambda e: e.amount)

    def above(self, limit):
        for e in self.expenses:
            if e.amount > limit:
                yield e

    def save(self, path):
        data = {"limit": self.limit, "expenses": []}
        for e in self.expenses:
            data["expenses"].append({"item": e.item, "amount": e.amount})
        with open(path, "w") as f:
            json.dump(data, f)

    def load(self, path):
        try:
            with open(path) as f:
                data = json.load(f)
        except FileNotFoundError:
            self.expenses = []
            return
        self.limit = data["limit"]
        self.expenses = []
        for d in data["expenses"]:
            self.add(d["item"], d["amount"])