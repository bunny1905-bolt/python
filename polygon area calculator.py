import math

def polygon_area(num_sides, side_length):
    if num_sides < 3:
        return "Error: A polygon must have at least 3 sides."

    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    area = (num_sides * side_length * apothem) / 2

    return area

# Example usage:
num_sides = int(input("Enter the number of sides of the polygon: "))
side_length = float(input("Enter the length of each side of the polygon: "))

result = polygon_area(num_sides, side_length)
print(f"The area of the polygon is: {result}")
