#!/usr/bin/python3
# File: 4-only_diff_elements.py
# Author: Oluwatobiloba Light


def only_diff_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A new set containing the common
        elements present in both input sets.
    """
    return [unique for unique in set(set_1) ^ set(set_2)]
