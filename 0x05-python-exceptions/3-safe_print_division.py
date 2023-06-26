#!/usr/bin/python3
# File: 3-safe_print_division.py
# Author: Oluwatobiloba Light


def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result.

    Args:
        a (int)
        b (int)

    Returns:
        - The value of the division, otherwise: None
    """
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        pass
    finally:
        print("Inside result: {:d}".format(result)) if type(result) == int\
            else print("Inside result: {}".format(result))
        return result
