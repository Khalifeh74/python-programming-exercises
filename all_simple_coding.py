# 1
# Calculating the average of numbers in a list:
# Create a list of numbers
# Then calculate the average of those numbers using sum() and len().

numbers = [5, 7, 10, 26, 28, 30, 50, 67]
total = sum(numbers)
count = len(numbers)
average = total / count

print("The sum of numbers is:", total)
print("The count of numbers is:", count)
print("The average of numbers is:", average)


# 2
# Removing duplicates from a list:
# Create a list with duplicate elements
# Then remove all duplicates using set().

numbers = [2, 2, 2, 5, 6, 8, 8, 12, 12, 15, 17, 17]
new_numbers = list(set(numbers))

print("The new list after removing duplicates is: ", new_numbers)


# 3
# Finding the largest and smallest number:
# Create a list of numbers and use max() and min() to find the largest and smallest number.

numbers = [5, 7, 10, 26, 28, 30, 50, 67]
largest = max(numbers)
smallest = min(numbers)

print("The Minimum is:", smallest)
print("The Maximum is:", largest)


# 4
# Reverse String:
# Create a string and use reversed() to reverse it.

string = "This is a text to reverse."
reversed_string = "".join(reversed(string))

print("The reversed string is:", reversed_string)


# 5
# Split a string based on a specific character:
# Create a string containing a sentence with spaces and use split() to split it into words.

string = "This is a string to split based on a specific character (space)"
split_string = string.split()

print("The words from the string after splitting are: \n", split_string)


# 6
# Convert numbers to strings:
# Receive an integer from the input and convert it to a string. Use str().

input_number = int(input("Enter a number: "))
string_conversion = str(input_number)

print("The number type was: ", type(input_number))
print("and it's type changed to: ", type(string_conversion))


# 7
# Reverse a string:
# Get a string from input and reverse it.
# (use a combination of str() and [::-1] notation).

input_string = input("Enter a string: ")
reversed_string = str(input_string[::-1])

print("The reversed string is: ", reversed_string)


# 8
# Number of repetitions of a character in a string:
# Receive a string and another character from the input.
# Then count the number of repetitions of that character in the string. Use count().

input_string = input("Enter a string: ")
char_to_count = input("Enter the character you want to count: ")
number_of_repetition = input_string.count(char_to_count)

print(f"The number of -{char_to_count}- repetition is: ", number_of_repetition)


# 9
# Convert string to lowercase and uppercase:
# Get a string from input and convert it to lowercase and uppercase.
# Use lower() and upper().

input_string = input("Enter a string: ")
lowercase_string = input_string.lower()
uppercase_string = input_string.upper()

print("The original string was: ", input_string)
print("The lowercase string is: ", lowercase_string)
print("The uppercase string is: ", uppercase_string)


# 10
# Finding the index of the first occurrence of a character in a string:
# Receive a string and another character from the input.
# Then find the index of the first occurrence of that character in the string. Use find().

input_string = input("Enter a string: ")
char_to_find = input("Enter a character to find its first occurrence: ")

index = input_string.find(char_to_find)

if index == -1:
    print(f"'{char_to_find}' was not found in the string.")
else:
    print(f"The first occurrence of '{char_to_find}' is at index {index}.")
