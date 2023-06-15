#!/usr/bin/python3
# File: 100-weight_average.py
# Author: Oluwatobiloba Light


def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of integer tuples.

    Args:
        my_list (list): A list of integer tuples
        in the format (<score>, <weight>).

    Returns:
        float: The weighted average of the scores in the list.
    """
    if (not isinstance(my_list, list)) or len(my_list) == 0:
        return 0

    average = 0
    size = 0
    for i in my_list:
        average += (i[0] * i[1])
        size += i[1]
    return average / size
