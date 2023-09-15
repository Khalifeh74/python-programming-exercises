# 3
# Inheritance Definition:
# Create a base class called "Animal" that has properties like name and type.
# Then create two subclasses named "Dog" and "Cat" that inherit from the "Animal" class and add their own properties.

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Dog(Animal):
    def __init__(self, name, type, owner, place):
        super().__init__(name, type)
        self.owner = owner
        self.place = place


class Cat(Animal):
    def __init__(self, name, type, sound, food):
        super().__init__(name, type)
        self.sound = sound
        self.food = food


dog = Dog("Doggy", "Chihuahua", "John", "Indoor")
cat = Cat("Catty", "Persian cat", "Meow!", "Meat")

print(
    f"{cat.name} is a {cat.type}, she sounds {cat.sound} and she eats {cat.food}.")
print(
    f"{dog.name} is a {dog.type}, his owner is {dog.owner} and he lives {dog.place}.")
