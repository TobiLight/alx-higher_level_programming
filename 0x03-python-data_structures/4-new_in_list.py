#!/usr/bin/python3
# File: 4-new_in_list.py
# Author: Oluwatobiloba Light


def new_in_list(my_list, idx, element):
    """
    Replaces an element at a specific index in the list with a new element.

    Args:
        my_list (list): The original list.
        idx (int): The index at which the element should be replaced.
        element: The new element to replace at the specified index.

    Returns:
        list: A copy of the original list with the element
        replaced at the given index, or a copy of the original list
        if the index is negative or out of range.

    Examples:
        my_list = [1, 2, 3, 4, 5]
        new_list = new_in_list(my_list, 2, "x")
        print(new_list)  # Output: [1, 2, "x", 4, 5]

        my_list = [1, 2, 3, 4, 5]
        new_list = new_in_list(my_list, -1, "x")
        print(new_list)  # Output: [1, 2, 3, 4, 5]
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    copy = my_list[:]
    copy[idx] = element
    return copy
