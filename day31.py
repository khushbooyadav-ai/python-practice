def countdown(n):
    while n > 0:
        yield n
        n = n - 1

gen = countdown(3)
assert next(gen) == 3
assert next(gen) == 2
assert next(gen) == 1
try:
    next(gen)
    assert False, "should have raised StopIteration"
except StopIteration:
    pass

assert list(countdown(3)) == [3, 2, 1]
assert list(countdown(0)) == []

total = 0
for n in countdown(4):
    total = total + n
assert total == 10

class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

class ExpenseBook:
    def __init__(self):
        self.expenses =[]

    def add(self, item, amount):
        self.expenses.append(Expense(item, amount))

    def above(self, limit):
        for e in self.expenses:
            if e.amount > limit:
                yield e

book = ExpenseBook()
book.add("tea", 20)
book.add("bus", 50)
book.add("pen", 10)
names = [e.item for e in book.above(15)]
assert names == ["tea", "bus"]

squares = (n * n for n in range(4))
assert sum(squares) == 14
print("all checks passed")
