#!/usr/bin/python3
# File: 5-square.py
# Author: Oluwatobiloba Light
"""Define a class Square."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        size(): Retrieve the size of the square.
        size(value): Set the size of the square.
        area(): Calculate and return the area of the square.
        my_print(): Print the square with '#' characters.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is less than 0.

    """

    def __init__(self, size=0):
        """
        Initializes a square instance with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with '#' characters.

        If size is equal to 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("#")
