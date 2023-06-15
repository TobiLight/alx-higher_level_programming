#!/usr/bin/python3
# File: 9-multiply_by_2.py
# Author: Oluwatobiloba Light


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary containing integer values.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})