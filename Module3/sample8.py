def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

# Get user input
l = float(input("Enter rectangle length: "))
w = float(input("Enter rectangle width: "))
area = calculate_rectangle_area(l, w)
print(f"Area of rectangle: {area}")
print(f"Docstring: {calculate_rectangle_area.__doc__}")