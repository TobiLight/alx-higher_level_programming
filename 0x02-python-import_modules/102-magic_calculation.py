#!/usr/bin/python3
# File: 102-magic_calculation.py
# Author: Oluwatobiloba Light


def magic_calculation(a, b):
    """Convert Bytecode to Python code"""
    from magic_calculation_102 import add, sub
    
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
