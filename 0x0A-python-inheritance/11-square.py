#!/usr/bin/python3
# File: 11-square.py
# Author: Oluwatobiloba Light
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): Private size of the square.

    Public Methods:
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
