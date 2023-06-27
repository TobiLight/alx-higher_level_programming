#!/usr/bin/python3
# File: 100-safe_print_integer_err.py
# Author: Oluwatobiloba Light


def safe_print_integer_err(value):
    """
    Prints an integer

    Args:
        value (any): can be any type (integer, string, etc.)

    Returns:
        - True if value has been correctly printed (it means
          the value is an integer)
        - Otherwise False and prints in stderr the error precede
          by Exception:
    """
    is_integer = False
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(str(e)))
        return False
