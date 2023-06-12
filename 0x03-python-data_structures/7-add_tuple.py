#!/usr/bin/python3
# File: 7-add_tuple.py
# Author: Oluwatobiloba Light


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples and returns a tuple with 2 integers.

    Args:
        tuple_a (tuple): The first tuple. Defaults to an empty tuple.
        tuple_b (tuple): The second tuple. Defaults to an empty tuple.

    Returns:
        tuple: A tuple containing the sum of corresponding
        elements from both input tuples.
        The first element is the addition of the first element
        of each tuple, and the second element is the addition
        of the second element of each tuple.
    """
    # Extract elements from tuple_a
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # Extract elements from tuple_b
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # Now you know the vibes 😉
    result = (a1 + b1, a2 + b2)
    return result
