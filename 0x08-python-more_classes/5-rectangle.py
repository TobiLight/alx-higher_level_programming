#!/usr/bin/python3
# File: 5-rectangle.py
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
        area(): Returns the area of a rectangle.
        perimeter(): Returns the perimeter of a rectangle.

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

    def area(self):
        """
        Calculates the area of a rectangle

        Returns:
            int: The area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle.add()

        Returns:
            int: The perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representatio of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        result = []
        for x in range(self.__height):
            for y in range(self.__width):
                result.append("#")
            if x != self.__height - 1:
                result.append("\n")
        return "".join(result)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Deletes an instance of a class Rectangle.
        """
        print("Bye rectangle...")
