#!/usr/bin/python3
# File: 0-lookup.py
# Author: Oluwatobiloba Light
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return the list of an object's available attributes and methods."""
    return (dir(obj))
