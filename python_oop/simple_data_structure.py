# 6
# Simple data structure:
# Create a class called "Student" that has attributes name and grade
# and create a method called "display_info" to display the student's information.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(F"{self.name} got {self.grade} in Database.")


student1 = Student("Zeynab", 19)
student2 = Student("Zahra", 18)

student1.display_info()
student2.display_info()
