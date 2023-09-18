# 10
# Using the public method:
# Create a class called "Rectangle" that has length and width properties.
# Then define a method called "calculate_area" that calculates the area of the rectangle and use it in different objects.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"The object area is: {area}.")
        return area


object1 = Rectangle(8, 4)
object2 = Rectangle(5, 2)
object3 = Rectangle(12, 6)

area1 = object1.calculate_area()
area2 = object2.calculate_area()
area3 = object3.calculate_area()
