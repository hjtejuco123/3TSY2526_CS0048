#Arrays in Polymorphism
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing circle."

class Square(Shape):
    def draw(self):
        return "Drawing square."

shapes = [Circle(), Square()]

# User Input
for shape in shapes:
    print(shape.draw())