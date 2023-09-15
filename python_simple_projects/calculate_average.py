# 1
# Calculating the average of numbers in a list:
# Create a list of numbers
# Then calculate the average of those numbers using sum() and len().


def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average


numbers = [5, 7, 10, 26, 28, 30, 50, 67]

total, count, average = calculate_average(numbers)

print("The total of numbers is:", total)
print("The count of numbers is:", count)
print("The average of numbers is:", average)
