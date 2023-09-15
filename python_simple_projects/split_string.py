# 5
# Split a string based on a specific character:
# Create a string containing a sentence with spaces and use split() to split it into words.


def split_string(string):
    split_the_string = string.split()
    return split_the_string


string = "This is a string to split based on a specific character (space)"

splited_string = split_string(string)

print("The words from the string after splitting are: \n", splited_string)
