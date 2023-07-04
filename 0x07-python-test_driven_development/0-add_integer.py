#!/usr/bin/python3
# File: 0-add_integer.py
# Author: Oluwatobiloba Light
"""Defines an integer addition function.
This function takes two arguments, `a` and `b`, and performs the addition
operation on them. If `a` is not provided, it defaults to 98. It raises a
TypeError If either `a` or `b` is not an integer.
"""


def add_integer(a, b=98):
    """Returns the sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
