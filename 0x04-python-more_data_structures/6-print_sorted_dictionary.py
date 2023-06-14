#!/usr/bin/python3
# File: 6-print_sorted_dictionary.py
# Author: Oluwatobiloba Light


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The dictionary to
        be printed.

    Returns:
        None
    """
    print("key: val" for key, val in sorted(
        a_dictionary.items(), key=lambda el: el[0]))
