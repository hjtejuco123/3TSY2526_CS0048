import math

def calculate_circle_area(radius):
    """This function calculates the area of a circle given its radius"""
    return math.pi * radius ** 2

# Get user input
radius = float(input("Enter the radius of the circle: "))
if radius < 0:
    print("Radius cannot be negative")
else:
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f}")