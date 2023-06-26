#!/usr/bin/python3
# File: 2-safe_print_list_integers.py
# Author: Oluwatobiloba Light


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.

    Returns:
        int: The real number of integers printed
    """
    num_of_integers_printed = 0

    for index in range(x):
        try:
            if type(my_list[index]) == int:
                print("{:d}".format(my_list[index]), end="")
                num_of_integers_printed += 1
        except IndexError:
            print("IndexError: list index out of range")
            return
    print()
    return num_of_integers_printed
