#!/usr/bin/python3
# File: 2-replace_in_list.py
# Author: Oluwatobiloba Light


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position

    Args:
        my_list (list): The input list
        idx (int): The index of the element to be replaced
        element (any): New element to be inserted at specific index

    Returns:
        list: The modified list if the index is valid
        otherwise returns the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
