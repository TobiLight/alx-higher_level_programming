#!/usr/bin/python3
# File: 8-class_to_json.py
# Author: Oluwatobiloba Light
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Returns the dictionary represntation of a simple data structure.
    """
    return obj.__dict__


if __name__ == "__main__":
    MyClass = __import__('8-my_class').MyClass
    MyClass2 = __import__('8-my_class_2').MyClass

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
    print("==========")
    m2 = MyClass2("John")
    m2.win()
    print(type(m2))
    print(m2)

    mj = class_to_json(m2)
    print(type(mj))
    print(mj)
