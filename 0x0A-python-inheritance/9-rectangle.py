#!/usr/bin/python3
# File: 9-rectangle.py
# Author: Oluwatobiloba Light
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): Private width of the rectangle.
        __height (int): Private height of the rectangle.

    Public Methods:
        area(self): Calculates and returns the area of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle description in the format '[Rectangle] <width>/<height>'.
        """
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)
