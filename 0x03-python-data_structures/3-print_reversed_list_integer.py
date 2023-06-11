#!/usr/bin/python3
# File: 3-print_reversed_list_integer.py
# Author: Oluwatobiloba Light


def print_reversed_list_integer(my_list=[]):
    """Prints elements of a list in reverse order.

    Args:
        my_list (list, optional): The input list. Defaults to [].

    Returns:
        list: The list in reverse
    """

    for i in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[i]))
