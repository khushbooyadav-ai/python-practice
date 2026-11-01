def unique_items(expenses):
    name = set()
    for item in expenses:
        name.add(item[0])
    return name

def total_by_item(expenses):
    totals = {}
    for item, amount in expenses:
        totals[item] = totals.get(item, 0) + amount
    return totals

def grand_total(expenses):
    total = 0
    for item, amount in expenses:
        total += amount
    return total
expenses = [("tea", 20), ("coffee", 30), ("tea", 15)]

data = [("tea",20), ("coffee", 30),("tea",20)]
assert total_by_item(data) == {"tea":40, "coffee":30}
assert unique_items(data) == {'tea', 'coffee'}
assert total_by_item([]) == {}
assert unique_items([]) == set()
print("all checks passed")