# 4
# Using defined functions in the class:
# Create a class called "Car" that has properties such as model, year of manufacture, and speed.
# Then define a method named "start_engine" to start the car engine
# and create another method named "stop_engine" to turn off the engine.

class Car:
    def __init__(self, model, year_of_manufacture, speed):
        self.model = model
        self. year_of_manufacture = year_of_manufacture
        self.speed = speed
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True
        print("Engine is started.")

    def stop_engine(self):
        self.engine_started = False
        print("Engine is stopped.")


car = Car("Lamborghini", "1963", "350 km/h")

car.start_engine()
car.stop_engine()

print(f"{car.model} was manufactured in {car.year_of_manufacture} and it can reach a top speed of {car.speed}.")
