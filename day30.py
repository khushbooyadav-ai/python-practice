def double(n):
    return n * 2

def apply_twice(func, x):
    return func(func(x))

assert apply_twice(double, 3) == 12

log = []

def logged(func):
    def wrapper(a, b):
        log.append(func.__name__)
        return func(a, b)
    return wrapper

@logged
def add(a, b):
    return a + b

@logged
def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

subtract = logged(subtract)

assert add(2, 3) == 5
assert multiply(2, 3) == 6
assert subtract(9, 4) == 5
assert log == ["add", "multiply", "subtract"]
print("all checks passed")