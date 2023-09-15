# 2
# Removing duplicates from a list:
# Create a list with duplicate elements
# Then remove all duplicates using set().


def remove_duplicates(primitive_list):
    new_list = list(set(primitive_list))
    return new_list


numbers = [2, 2, 2, 5, 6, 8, 8, 12, 12, 15, 17, 17]

new_numbers = remove_duplicates(numbers)

print("The new list after removing duplicates is: ", new_numbers)
