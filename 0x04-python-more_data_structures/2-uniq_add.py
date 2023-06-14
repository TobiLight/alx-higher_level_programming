#!/usr/bin/python3
# File: 2-uniq_add.py
# Author: Oluwatobiloba Light


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list
    (only once for each integer).

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The sum of all unique integers in the list.
    """
    new_list = set(my_list)
    result = 0
    for unique in new_list:
        result += unique
    return result
