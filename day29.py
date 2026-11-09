class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

expenses = [Expense("tea", 20), Expense("bus", 50), Expense("pen",10)]

by_amount = sorted(expenses, key=lambda e: e.amount)
assert by_amount[0].item == "pen"
assert expenses[0].item == "tea"

by_name = sorted(expenses, key=lambda e: e.item)
assert by_name[0].item == "bus"

biggest = max(expenses, key=lambda e: e.amount)
assert biggest.item == "bus"

smallest = min(expenses, key=lambda e: e.amount)
assert smallest.item == "pen"

amount = [e.amount for e in expenses]
assert amount == [20, 50, 10]

big = [e for e in expenses if e.amount > 15]
assert len(big) == 2

print("all checks passed")