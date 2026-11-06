import json
import os


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

book = ExpenseBook()
book.add("tea", 20)
book.add("bus", 50)
book.save("day27_test.json")

book2 = ExpenseBook()
book2.load("day27_test.json")
assert len(book2.expenses) == 2
assert book2.expenses[1].item == "bus"
assert book2.expenses[1].amount == 50

empty = ExpenseBook()
empty.load("no_such_file.json")
assert len(empty.expenses) == 0

os.remove("day27_test.json")

print("all checks passed")