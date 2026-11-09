class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = [Student("ravi", 60), Student("zoya", 80), Student("ava", 90)]

by_marks = sorted(students, key=lambda s: s.marks)
assert by_marks[0].name == "ravi"
assert students[0].name == "ravi"

by_name = sorted(students, key=lambda s: s.name)
assert by_name[0].name == "ava"

biggest = max(students, key=lambda s: s.marks)
assert biggest.name == "ava"

smallest = min(students, key=lambda s: s.marks)
assert smallest.name == "ravi"

marks = [s.marks for s in students]
assert marks == [60, 80, 90]

big = [s for s in students if s.marks >= 70]
assert len(big) == 2

passed_name = [s.name for s in students if s.marks>=70]
assert passed_name == ["zoya", "ava"]

print("all checkd passed")
