#!/usr/bin/python3
# File: 101-add_attribute.py
# Author: Oluwatobiloba Light
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible. Raises a
    TypeError exception with the message "can't add new attribute" if the
    object can't have a new attribute.

    Args:
        obj: The object to add the attribute to.
        attr_name (str): The name of the attribute to be added.
        attr_value: The value of the attribute to be added.

    Raises:
        TypeError: If the object can't have a new attribute.

   """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
