class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return f"{self.item}: {self.amount}"

def amount_of(e):
        return e.amount

class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, item, amount):
        self.expenses.append(Expense(item, amount))

    def sorted_by_amount(self):
        return sorted(self.expenses, key=amount_of, reverse=True)

    def above(self, limit):
        result = []
        for e in self.expenses:
            if e.amount > limit:
                result.append(e)
        return result

    def top(self, n):
        return self.sorted_by_amount()[:n]
    
book = ExpenseBook()
book.add("tea", 20)
book.add("bus", 50)
book.add("pen", 10)
assert str(book.expenses[0]) == "tea: 20"
ordered = book.sorted_by_amount()
assert ordered[0].item == "bus"
assert ordered[2].item == "pen"
assert book.expenses[0].item == "tea"
assert len(book.above(15)) == 2
assert book.above(100) == []
assert len(book.top(2)) == 2
assert book.top(2)[0].item == "bus"
assert book.top(2)[1].item == "tea"
assert len(book.top(10)) == 3
print("all checks passed")