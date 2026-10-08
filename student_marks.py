marks = {}

count = int(input("How many students? "))

for i in range(count):
    name = input("Student name: ")
    score = int(input("Marks: "))
    marks[name] = score

for name, score in marks.items():
    print(name, score)

average = sum(marks.values()) / len(marks)
print(f"Class average: {average:.1f}")

topper = max(marks, key=marks.get)
print("Topper:", topper, "with", marks[topper], "marks")