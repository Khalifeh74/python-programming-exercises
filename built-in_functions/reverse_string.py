# 4
# Reverse String:
# Create a string and use reversed() to reverse it.

def reverse_string(string):
    reversed_string = "".join(reversed(string))
    return reversed_string


string = "This is a text to reverse."

reversed_string = reverse_string(string)

print("The reversed string is:", reversed_string)
