#!/usr/bin/python3
# File: 1-rectangle.py
# #Author: Oluwatobiloba Light
"""Defines a Rectangle."""


class Rectangle:
    """
    Represents a Rectangle

    Attributes:
        __width (int): The width of the rectangle
        __height (int): The height of the rectangle

    Methods:
        width(property): Retrieves the width of a rectangle
        width(setter): Sets the width of a rectangle
        height (property): Retrieve the height of the rectangle.
        height (setter): Set the height of the rectangle.

    Raises:
        TypeError: If the width or height is not an integer.
        ValueError: If the width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance with an optional width and height

        Args:
            width (int, optional): Width of a rectangle. Defaults to 0.
            height (int, optional): Height of a rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of a rectangle

        Returns:
            int: The width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of a rectangle.

        Args:
            value (int): The width of a rectangle.

        Raises:
            TypeError: If the provided width is not an integer.
            ValueError: If the provided width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of a rectangle

        Returns:
            int: The height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of a rectangle.

        Args:
            value (int): The height of a rectangle.

        Raises:
            TypeError: If the provided height is not an integer.
            ValueError: If the provided height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
