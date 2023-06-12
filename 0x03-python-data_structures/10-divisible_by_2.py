#!/usr/bin/python3
# File: 10-divisible_by_2.py
# Author: Oluwatobiloba Light


def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The input list containing integers.

    Returns:
        list: A new list of the same size as the original list,
              where each element is True or False depending on whether
              the corresponding integer in the original list is a
              multiple of 2.
    """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
