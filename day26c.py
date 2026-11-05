numbers = [30, 90, 50]
best = None
for n in numbers:
    if best is None or n > best:
        best = n
print(best)