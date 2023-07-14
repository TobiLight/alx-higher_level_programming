#!/usr/bin/python3
# File: base.py
# Author: Oluwatobiloba Light
"""This module defines a “base” of all other classes in this project"""


class Base():
    """
    Represents the base for all the other classes in this project

    Attr:
        __nb_objects (int): Number of instantiated classes
        id (int, optional): ID of the class. Defaults to None

    Methods:
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class

        Args:
            id (int, optional): ID of the class. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
