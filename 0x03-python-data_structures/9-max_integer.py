#!/usr/bin/python3
# File: 9-max_integer.py
# Author: Oluwatobiloba Light


def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list.

    Args:
        my_list (list): The input list containing integers.

    Returns:
        int or None: The biggest integer in the list, or
        None if the list is empty.
    """
    max_num = my_list[0] if len(my_list) > 0 else None
    for i in range(1,len(my_list)):
        if max_num < my_list[i]:
            max_num = my_list[i]
    return max_num
        