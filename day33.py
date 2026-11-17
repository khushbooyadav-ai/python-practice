def grade(marks):
    if marks < 0 or marks > 100:
        raise ValueError("marks must be between 0 and 100.")
    if marks >= 80:
        return "A"
    if marks >= 60:
        return "B"
    if marks >= 40:
        return "C"
    return "F"