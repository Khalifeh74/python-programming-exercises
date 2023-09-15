# 3
# Finding the largest and smallest number:
# Create a list of numbers and use max() and min() to find the largest and smallest number.

def find_min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest


numbers = [7, 30, 67, 26, 5, 28, 10, 50]

smallest, largest = find_min_max(numbers)

print("The Minimum is:", smallest)
print("The Maximum is:", largest)
