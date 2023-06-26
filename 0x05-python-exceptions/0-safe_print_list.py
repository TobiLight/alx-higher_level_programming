#!/usr/bin/python3
# File: 0-safe_print_list.py
# Author: Oluwatobiloba Light


def safe_print_list(my_list=[], x=0):
    """
    Safely prints the elements of a list up to a specified index.

    Args:
        my_list (list, optional): The list to be printed. Defaults
                                  to an empty list.
        x (int, optional): The maximum number of elements to print.
                           Defaults to 0.

    Returns:
        int: The actual number of elements printed.
    """
    try:
        length_of_list = 0
        [length_of_list := length_of_list + 1 for _ in my_list]
        if x <= 0 or x > length_of_list:
            [print(my_list[elements], end="")
            for elements in range(0, length_of_list)]
            print()
        else:
            [print(my_list[elements], end="") for elements in range(0, x)]
            print()
    except:
        print("An unknown error has occured!")
    
    return length_of_list if x <= 0 else x