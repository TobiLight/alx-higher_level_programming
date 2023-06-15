#!/usr/bin/python3
# File: 8-simple_delete.py
# Author: Oluwatobiloba Light


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to be modified.
        key (str): The key to be deleted. Defaults to an empty string.

    Returns:
        None
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
