class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

def evens(limit):
    n = 0
    while n < limit:
        yield n
        n  = n + 2

class MarksBook:
    def __init__(self):
        self.students = []

    def add(self, name, marks):
        self.students.append(Student(name, marks))


    def at_least(self, limit):
        for s in self.students:
            if s.marks >= limit:
                yield s

assert list(evens(7)) == [0, 2, 4, 6]
assert list(evens(0)) == []

book = MarksBook()
book.add("asha", 80)
book.add("ravi", 60)
book.add("zoya", 90)
names = [s.name for s in book.at_least(80)]
assert names == ["asha", "zoya"] 
first_pass = next(s for s in book.at_least(80))
assert first_pass.name == "asha"
print("all checks passed")