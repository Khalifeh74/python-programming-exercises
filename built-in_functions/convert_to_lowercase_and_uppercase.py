# 9
# Convert string to lowercase and uppercase:
# Get a string from input and convert it to lowercase and uppercase.
# Use lower() and upper().


def convert_to_lowercase_and_uppercase():
    input_string = input("Enter a string: ")
    lowercase_string = input_string.lower()
    uppercase_string = input_string.upper()
    return input_string, lowercase_string, uppercase_string


input_string, lowercase_string, uppercase_string = convert_to_lowercase_and_uppercase()

print("The original string was: ", input_string)
print("The lowercase string is: ", lowercase_string)
print("The uppercase string is: ", uppercase_string)
