# 2
# Calculating area and perimeter of a rectangle using class:
# Create a class called "Rectangle" that has two properties as length and width.
# Then create two methods named "calculate_area" and "calculate_perimeter" to calculate the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


rectangle1 = Rectangle(8, 5)

area1 = rectangle1.calculate_area()
perimeter1 = rectangle1.calculate_perimeter()

print(f"The rectangle area is {area1}, and it's perimeter is {perimeter1}.")
