#!/usr/bin/python3
# File: 10-best_score.py
# Author: Oluwatobiloba Light


def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary containing integer values.

    Returns:
        str or None: The key with the biggest integer value. If no score is found, returns None.
    """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    result = list(a_dictionary.keys())[0]
    biggest_scoe = a_dictionary[result]
    for k, v in a_dictionary.items():
        if v > biggest_score:
            biggest_score = v
            result = k
    return result
