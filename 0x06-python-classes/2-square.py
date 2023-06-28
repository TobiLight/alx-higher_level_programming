#!/usr/bin/python3
# File: 2-square.py
# Author: Oluwatobiloba Light
"""Define a class Square."""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size