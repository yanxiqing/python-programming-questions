"""
Problem 1: Write a function that returns the largest element in a list.

Note: In this Python implementation, numbers, booleans or strings are considered as the valid list elements
"""


def get_largest_list_element(input_list):

    # Check against non-list input
    if not(isinstance(input_list, list)):
        return None

    return input_list


if __name__ == "__main__":

    # Test function
    list_booleans = [False, True, False, True]  # Test returning the first occurrence of the largest element (True)
    list_numbers = [4, 3, 2, 1, 8, 6]
    list_strings = ["a", "z", "home", "ccc", "zzz"]
    list_combined = [3, 4, "yes", "45", 56]
    list_inputs = [23, list_booleans, list_numbers, list_strings, list_combined]

    for var in list_inputs:
        print("- Input: " + str(var) + ", Output: " + str(get_largest_list_element(var)))

