import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class MarksBook:
    def __init__(self):
        self.students = []

    def add(self, name, marks):
        self.students.append(Student(name, marks))

    def save(self, path):
        data = []
        for s in self.students:
            data.append({"name": s.name, "marks": s.marks})
        with open(path, "w") as f:
            json.dump(data, f)

    def load(self, path):
        try:
            with open(path) as f:
                data = json.load(f)
        except FileNotFoundError:
            self.students = []
            return
        self.students = []
        for d in data:
            self.add(d["name"], d["marks"])