# 3
# Using private properties:
# Create a class called "Employee" that has the name and employee number attributes as private.
# Then create a method to display employee information and use private properties securely.

class Employee:
    def __init__(self, name, employee_number):
        self.__name = name
        self.__employee_number = employee_number

    def display_info(self):
        print(F"{self.get_name()} number is {self.get_employee_number()}.")

    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__employee_number


employee = Employee("Zeynab", "Z123456")

employee.display_info()
