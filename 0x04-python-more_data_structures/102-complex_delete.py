#!/usr/bin/python3
# File: 102-complex_delete.py
# Author: Oluwatobiloba Light


def complex_delete(a_dictionary, value):
    """
    Delete keys with a specific value from a dictionary.

    Args:
        a_dictionary (dict): The dictionary from which keys will be deleted.
        value: The value to search for and delete all associated keys.

    Returns:
        None.
    """
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
