# 6
# Convert numbers to strings:
# Receive an integer from the input and convert it to a string. Use str().

def convert_number_to_string():
    input_number = int(input("Enter a number: "))
    string_conversion = str(input_number)
    return input_number, string_conversion


input_number, converted_result = convert_number_to_string()

print("The number type was: ", type(input_number))
print("and it's type changed to: ", type(converted_result))
