#!/usr/bin/python3
# File: 1-element_at.py
# Author: Oluwatobiloba Light


def element_at(my_list, idx):
    """Get the element at the specified index in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the element to retrieve.

    Returns:
        Any: The element at the specified index, or None if idx is negative or out of range.
    """
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    
    return my_list[idx]