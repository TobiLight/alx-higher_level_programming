#!/usr/bin/python3
# File: 4-square.py
# Author: Oluwatobiloba Light
"""Define a class Square."""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
