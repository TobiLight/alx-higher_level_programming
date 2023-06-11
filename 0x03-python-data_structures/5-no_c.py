#!/usr/bin/python3
# File: 5-no_cpy.py
# Author: Oluwatobiloba Light


def no_c(my_string):
    """
    Removes all occurrences of the letter 'c'
    (both uppercase and lowercase) from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The new string with all 'c' characters removed.
    """
    res = ""
    # for char in my_string:
    #     if char != 'C' and char != 'c':
    #         res += char
    # return res
    res = "".join([char for char in my_string if char != "C" and char != 'c'])
    return res
