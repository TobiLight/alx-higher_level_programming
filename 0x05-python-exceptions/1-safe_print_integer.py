#!/usr/bin/python3
# File: 1-safe_print_integer.py
# Author: Oluwatobiloba Light


def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value (any): can be any type (integer, string, etc.)
        
    Returns: True if value has been correctly printed
             (it means the value is an integer)
    """
    correctly_printed = False
    
    try:
        if isinstance(abs(value), int):
            print("{:d}".format(value))
            correctly_printed = True
        else:
            correctly_printed = False
    except TypeError:
        pass
    return correctly_printed
