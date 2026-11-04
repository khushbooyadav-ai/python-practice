class Counter:
    def __init__(self):
        self.count = 0

    def add(self, amount):
        self.count = self.count + amount

    def __str__(self):
        return f"Counter is at {self.count}"

c = Counter()
c.add(5)
c.add(3)
print(c.count)
print(c)

other = Counter()
print(other.count) == 0

assert c.count == 8
assert other.count == 0
print("all checks passed")
