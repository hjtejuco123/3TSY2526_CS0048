#Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# User Input
x1, y1 = map(int, input("Enter first point (x y): ").split())
x2, y2 = map(int, input("Enter second point (x y): ").split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
print("Sum of points:", p1 + p2)