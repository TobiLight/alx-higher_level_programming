#!/usr/bin/python3
# File: 1-calculation.py
# Author: Oluwatobiloba Light
if __name__ == "__main__":
    """Prints the sum, difference, product and division of 10 & 5"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
