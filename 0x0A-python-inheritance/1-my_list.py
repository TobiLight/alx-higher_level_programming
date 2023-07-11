#!/usr/bin/python3
# File: 1-my_list.py
# Author: Oluwatobiloba Light
"""Defines an inherited class MyList"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
