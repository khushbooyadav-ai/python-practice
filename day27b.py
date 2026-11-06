import json
import os


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class MarksBook:
    def __init__(self):
        self.students = []

    def add(self, name, marks):
        self.students.append(Student(name, marks))

    def average(self):
        if len(self.students) == 0:
            raise ValueError("no students.")
        total = 0
        for s in self.students:
            total = total + s.marks
        return total / len(self.students)

    def find(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def delete(self, name):
        s = self.find(name)
        if s is None:
            raise ValueError("no such student.")
        self.students.remove(s)

    def save(self, path):
        data =[]
        for s in self.students:
            data.append({"name": s.name, "marks": s.marks})
        with open(path, "w") as f:
            json.dump(data, f)

    def load(self, path):
        with open(path) as f:
            data = json.load(f)
        self.students = []
        for d in data:
            self.add(d["name"], d["marks"])

book = MarksBook()
book.add("asha", 80)
book.add("ravi", 60)
assert book.average() == 70
assert book.find("ravi").marks == 60
assert book.find("zoya") is None
book.delete("asha")
assert book.average() == 60
try:
    book.delete("zoya")
    assert False, "should have raised ValueError"
except ValueError:
    pass
try:
    MarksBook().average()
    assert False, "should have raised ValueError"
except ValueError:
    pass

book = MarksBook()
book.add("asha", 80)
book.add("ravi", 60)
book.save("day27b_test.json")

book2 = MarksBook()
book2.load("day27b_test.json")
assert len(book2.students) == 2
assert book2.find("ravi").marks == 60
assert book2.average() == 70
os.remove("day27b_test.json")

print("all checks passed")