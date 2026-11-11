def loud(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

@loud
def greet(name):
    return "hello " + name

print(greet("asha"))