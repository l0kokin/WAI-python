import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return None


class Rectangle(Shape):
    def __init__(self, width, height, name):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return round((self.radius ** 2 * math.pi), 2)


def print_area(shape):
    print(f"The area of {shape.name} is {shape.area()}.")


rectangle1 = Rectangle(5, 10, "Rectangle Bob")
circle1 = Circle(2, "Circle Sali")
print_area(rectangle1)
print_area(circle1)