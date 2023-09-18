# 4
# Inheritance:
# Create a base class called "Vehicle" that has properties like speed and color.
# Then create two subclasses named "Car" and "Bicycle" that inherit from the main class and add your own properties and methods.

class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def display_info(self):
        print(F"Your vihicle speed is {self.speed} and it is {self.color}.")


class Car(Vehicle):
    def __init__(self, speed, color, brand, model):
        super().__init__(speed, color)
        self.brand = brand
        self.model = model

    def display_info(self):
        super().display_info()
        print(F"Your car is a {self.brand} {self.model}.")

    def number_of_passengers(self):
        print("You can fit 4 passengers in a car.")


class Bicycle(Vehicle):
    def __init__(self, speed, color, model, price):
        super().__init__(speed, color)
        self.model = model
        self.price = price

    def display_info(self):
        super().display_info()
        print(F"this is a {self.price} {self.model} bike.")

    def sound(self):
        print("You can install a ring bell on your bike.")


car = Car(200, "blue", "BMW", "X5")
bicycle = Bicycle(10, "red", "Mountain", "$4000")

car.display_info()
car.number_of_passengers()
print("-"*40)
bicycle.display_info()
bicycle.sound()
