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
            raise ValueError("no such students.")
        self.students.remove(s)    