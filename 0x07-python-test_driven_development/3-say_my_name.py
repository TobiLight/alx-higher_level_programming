#!/usr/bin/python3
# File: 3-say_my_name.py
# Author: Oluwatobiloba Light
"""Prints the provided first name and last name."""


def say_my_name(first_name, last_name=""):
    """Prints the provided first name and last name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed.
            Defaults to an empty string.

    Raises:
        TypeError: first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {f} {l}".format(f=first_name, l=last_name))
