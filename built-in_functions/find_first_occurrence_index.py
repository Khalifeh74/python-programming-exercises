# 10
# Finding the index of the first occurrence of a character in a string:
# Receive a string and another character from the input.
# Then find the index of the first occurrence of that character in the string. Use find().


def find_first_occurrence_index():
    input_string = input("Enter a string: ")
    char_to_find = input("Enter a character to find its first occurrence: ")
    index = input_string.find(char_to_find)
    return char_to_find, index


char_to_find, index = find_first_occurrence_index()

if index == -1:
    print(f"'{char_to_find}' was not found in the string.")
else:
    print(f"The first occurrence of '{char_to_find}' is at index {index}.")
