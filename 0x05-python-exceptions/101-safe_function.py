#!/usr/bin/python3
# File: 100-safe_print_integer_err.py
# Author: Oluwatobiloba Light


import sys


def safe_function(fct, *args):
    """
    Safely executes a given function with the provided
    arguments and handles any exceptions.

    Args:
        fct (callable): The function to be executed.
        *args: Variable-length arguments to be passed to the function.

    Returns:
        Any: The return value of the function if it executes successfully,
             or None otherwise.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return None
