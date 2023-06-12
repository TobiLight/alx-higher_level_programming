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
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return ()
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        return (tuple_a[0] + tuple_b[0], 0)
    elif len(tuple_a) < 1 and len(tuple_b) > 0:
        return tuple_b
    elif len(tuple_a) > 0 and len(tuple_b) < 1:
        return tuple_a
    elif len(tuple_a) > 1 and len(tuple_b) == 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif len(tuple_a) == 1 and len(tuple_b) > 1:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    else:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
