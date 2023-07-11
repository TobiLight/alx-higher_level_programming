#!/usr/bin/python3
# File: 100-my_int.py
# Author: Oluwatobiloba Light
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    MyInt class that inherits from int.
    """

    def __eq__(self, other):
        """
        Override the == operator to invert its behavior.

        Args:
            other: The object to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to invert its behavior.

        Args:
            other: The object to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
