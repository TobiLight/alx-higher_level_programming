#!/usr/bin/python3
# File: 0-safe_print_list.py
# Author: Oluwatobiloba Light


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
        my_list (list, optional): The list to be printed. Defaults
                                  to an empty list.
        x (int, optional): The maximum number of elements to print.
                           Defaults to 0.

    Returns:
        int: The actual number of elements printed.
    """
    length_of_list = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            length_of_list += 1
        except IndexError:
            break
    print()
    return length_of_list