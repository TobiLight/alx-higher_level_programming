#!/usr/bin/python3
# File: 10-best_score.py
# Author: Oluwatobiloba Light


def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in
    a dictionary.

    Args:
        a_dictionary (dict): The dictionary containing
        integer values.

    Returns:
        str or None: The key with the biggest integer value.
        If no score is found, returns None.
    """
    biggest_score = None
    biggest_key = None

    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if biggest_score is None or value >
            biggest_score:
                biggest_score = value
                biggest_key = key

    return biggest_key
