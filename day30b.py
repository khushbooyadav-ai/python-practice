calls = {"count": 0}

def counted(func):
    def wrapper(n):
        calls["count"] = calls["count"] + 1
        return func(n)
    return wrapper

@counted
def square(n):
    return n * n

@counted
def negate(n):
    return -n

def positive_only(func):
    def wrapper(n):
        if n <= 0:
            raise ValueError("must be positive.")
        return func(n)
    return wrapper

@positive_only
def half(n):
    return n/2

assert square(4) == 16
assert negate(5) == -5
assert square(3) == 9
assert calls["count"] == 3
assert half(10) == 5
try:
    half(-4)
    assert False, "should have raised ValueError"
except ValueError:
    pass
print("all checks passed")

