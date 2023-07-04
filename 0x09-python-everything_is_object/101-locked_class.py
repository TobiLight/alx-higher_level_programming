#!/usr/bin/python3
# File: 101-locked_class.py
# Author: Oluwatobiloba Light
"""Defines a locked class."""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
