#!/usr/bin/python3
# File: 3-common_elements.py
# Author: Oluwatobiloba Light


def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A new set containing the common elements
        present in both input sets.
    """
    return [set(set_1) & set(set_2)]
