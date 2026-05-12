def rectangle_properties(length, width):
    """Calculate area and perimeter of a rectangle"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returns a tuple

# Get user input
l = float(input("Enter rectangle length: "))
w = float(input("Enter rectangle width: "))
a, p = rectangle_properties(l, w)
print(f"Area: {a}, Perimeter: {p}")