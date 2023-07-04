#!/usr/bin/python3
# File: 19-copy_list.py
# #Author: Oluwatobiloba Light
"""Returns copy of a list"""


def copy_list(l):
    """
    Return a copy of a list.

    Args:
        l (list): The input list to be copied.

    Returns:
        A new list with the same elements as the original list.

    """
    new_list = l[:]
    return new_list
