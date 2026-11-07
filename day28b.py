class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}: {self.marks}"

def marks_of(s):
    return s.marks

class MarksBook:
    def __init__(self):
        self.students = []

    def add(self, name, marks):
        self.students.append(Student(name, marks))

    def sorted_by_marks(self):
        return sorted(self.students, key=marks_of, reverse=True)

    def at_least(self, limit):
        result = []
        for s in self.students:
            if s.marks >= limit:
                result.append(s)
        return result

book = MarksBook()
book.add("asha", 80)
book.add("zoya", 60)
book.add("ravi", 90)
assert str(book.students[0]) =="asha: 80"
ordered = book.sorted_by_marks()
assert ordered[0].name == "ravi"
assert ordered[2].name == "zoya"
assert book.students[0].name =="asha"
assert len(book.at_least(80)) == 2
assert book.at_least(100) == []
print("all checka passed")