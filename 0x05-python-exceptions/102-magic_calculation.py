#!/usr/bin/python3
# File: 100-safe_print_integer_err.py
# Author: Oluwatobiloba Light


def magic_calculation(a, b):
    """
    Function that does magic calculation like bytecode

    Args:
        a (int): Integer
        b (int): Integer

    Returns:
        - Integer
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a + b) ** i / i
        except:
            result = result + a + b
            break
    return result
