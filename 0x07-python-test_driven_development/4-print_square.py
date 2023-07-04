#!/usr/bin/python3
# File: 4-print_square.py
# Author: Oluwatobiloba Light
"""Prints a square made of '#' characters of a specified size."""


def print_square(size):
    """
    Prints a square with the character '#' of the specified size.

    Args:
        size (int): The size length of the square.

    Returns:
        None

    Raises:
        TypeError: If the size is not an integer or a float.
        ValueError: If the size is less than 0 (for integers) or if
                    it is a float less than 0.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size < 0 and isinstance(size, float):
        raise TypeError('size must be an integer')

    for x in range(size):
        print('#' * size)
