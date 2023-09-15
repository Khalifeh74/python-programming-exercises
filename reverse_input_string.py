# 7
# Reverse a string:
# Get a string from input and reverse it.
# (use a combination of str() and [::-1] notation).

def reverse_input_string():
    input_string = input("Enter a string: ")
    reversed_string = str(input_string[::-1])
    return reversed_string


reversed_result = reverse_input_string()

print("The reversed string is: ", reversed_result)
