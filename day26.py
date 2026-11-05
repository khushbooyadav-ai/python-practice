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

    def biggest(self):
        best = None
        for e in self.expenses:
            if best is None or e.amount > best.amount:
                best = e
        return best

book = ExpenseBook()
book.add("tea", 20)
book.add("bus", 50)
assert book.total() == 70
assert book.find("bus").amount == 50
assert book.find("pen") is None
book.delete("tea")
assert book.total() == 50
try:
    book.delete("pen")
    assert False, "should have raised ValueError"
except ValueError:
    pass
assert book.biggest().item == "bus"
assert ExpenseBook().biggest() is None
print("all checks passed")

     
    