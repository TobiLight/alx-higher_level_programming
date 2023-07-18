#!/usr/bin/python3
# File: rectangle.py
# Author: Oluwatobiloba Light
"""This module defines a Rectangle class inherited from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle class

    Args:
        Base (obj): Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets the value of a rectangle width

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of a rectangle width

        Args:
            value (int): Width of rectangle

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the value of a rectangle height

        Returns:
            int: Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of a rectangle height

        Args:
            value (int): Height of rectangle

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the value of x

        Returns:
            int: Value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value for x

        Args:
            value (int): Value of x

        Raises:
            TypeError: Must be an integer
            ValueError: Must be greater than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the value of y

        Returns:
            int: Value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value for Y

        Args:
            value (int): Value of y

        Raises:
            TypeError: Must be an integer
            ValueError: Must be greater than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of a rectangle

        Returns:
            The area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character '#'
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for _ in range(self.y):
            print("")
        for i in range(self.__height):
            for _ in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Update the Rectangle.

        Args:
            *args (int): attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): key/value pairs of attributes.
        """
        if len(args) < 1:
            for key, val in kwargs.items():
                if key == "width":
                    self.width = val
                if key == 'height':
                    self.height = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val
                if key == 'id':
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = val
        elif len(args) >= 1:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i ==1:
                    self.width = args[i]
                elif i ==2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
                      

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle

        Returns:
            obj: Dictionary representation of the Rectangle instance.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        String representation of the class

        Returns:
            str: String JSON representation of the class
        """
        return "".join("[{}] ({}) {}/{} - {}/{}"
                       .format(type(self).__name__, self.id, self.__x,
                               self.__y, self.__width, self.__height))
