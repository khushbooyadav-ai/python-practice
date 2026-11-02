def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None

def first_item(items):
    try:
        return items[0]
    except IndexError:
        return None

def parse_age(text):
    age = int(text)
    if age<0 or age>120:
        raise ValueError("age must be between 0 and 120")
    return age

try:
    parse_age(200)
except ValueError as error:
    print("Bad input:", error)

def parse_expense(line):
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError("line must look like item,amount")
    return parts[0].strip(), float(parts[1])

assert parse_expense("tea,20") == ("tea", 20)
for bad in ["tea", "tea,20,30", ""]:
    try:
        parse_expense(bad)
        assert False, "should have raised ValueError"
    except ValueError:
        pass
     

assert first_item(["tea", "coffee"]) == "tea"
assert first_item([]) is None
assert safe_int("45") == 45
assert safe_int("abc") is None
assert safe_int("") is None
assert safe_divide(10, 2) == 5
assert safe_divide(10, 0) is None
assert parse_expense(" tea , 20 ") == ("tea", 20)
print("all checks passed")