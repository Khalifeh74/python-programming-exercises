# 1
# Create a simple class:
# Create a simple class called "Person" that has properties like name, age, and occupation.
# Then create instances of this class and set their properties.

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation


person1 = Person("Zeynab", 28, "teacher")
person2 = Person("Zahra", 29, "principal")

print(
    f"Person1 name is {person1.name}, with {person1.age} years old and works as a {person1.occupation}.")
print(
    f"Person2 name is {person2.name}, with {person2.age} years old and works as a {person2.occupation}.")
