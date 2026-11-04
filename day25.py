class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def with_tax(self, rate):
        return self.price + self.price * rate

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width + self.height)

tea = Product("tea", 20)
print(tea.name)
print(tea.with_tax(0.1))

r = Rectangle(3, 4)
assert r.area() == 12
assert r.perimeter() == 14
print("all checks passed")
