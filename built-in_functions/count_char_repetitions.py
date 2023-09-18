# 8
# Number of repetitions of a character in a string:
# Receive a string and another character from the input.
# Then count the number of repetitions of that character in the string. Use count().

def count_char_repetitions():
    input_string = input("Enter a string: ")
    char_to_count = input("Enter the character you want to count: ")
    number_of_repetition = input_string.count(char_to_count)
    return char_to_count, number_of_repetition


char_to_count, repetition_count = count_char_repetitions()

print(f"The '{char_to_count}' character is repeated {repetition_count} times.")
