import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_square_area(side):
    return side * side

def calculate_circle_area(radius):
    return math.pi * radius * radius

# Example usage:
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print(f"Area of rectangle: {calculate_rectangle_area(length, width)}")

side = float(input("Enter side length of square: "))
print(f"Area of square: {calculate_square_area(side)}")

radius = float(input("Enter radius of circle: "))
print(f"Area of circle: {calculate_circle_area(radius)}")
