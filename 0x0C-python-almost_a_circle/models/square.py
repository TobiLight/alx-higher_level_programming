#!/usr/bin/python3
# File: square.py
# Author: Oluwatobiloba Light
"""This module defines a Square class inherited from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square class.

    Args:
        Rectangle (obj): Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance

        Args:
            size (int): Size of the square
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): Id of an instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of a Square

        Returns:
            int: Size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of a Square

        Args:
            value (int): Size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update values of an instance

        Args:
            args (any): Non-keyword arguments (id, size, x, y)
            kwargs (any): Key-worded arguments
        """
        if len(args) < 1:
            for key, val in kwargs.items():
                if key == "size":
                    self.width = val
                    self.height = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val
                if key == 'id':
                    self.__init__(self.size, self.x, self.y, id=val)
        elif len(args) >= 1:
            for count in range(len(args)):
                if count == 0:
                    self.__init__(self.size, self.x, self.y, id=args[count])
                if count == 1:
                    self.size = args[count]
                if count == 2:
                    self.x = args[count]
                if count == 3:
                    self.y = args[count]

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square

        Returns:
            obj: Dictionary representation of the Square instance.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return "".join("[{}] ({}) {}/{} - {}"
                       .format(type(self).__name__,
                               self.id, self.x, self.y, self.width))
