#!/usr/bin/python3
# File: 7-update_dictionary.py
# Author: Oluwatobiloba Light


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to be updated.
        key (str): The key to be replaced or added.
        value (any): The value to be assigned to the key.

    Returns:
        None
    """
    a_dictionary[key] = value
    return (a_dictionary)
