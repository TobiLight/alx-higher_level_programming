#!/usr/bin/python3
# File: 0-read_file.py
# Author: Oluwatobiloba Light
"""Defines a function to read text from file"""


def read_file(filename=''):
    """
    Reads a text from file

    Args:
        filename (str, optional): Name of the file. Defaults to ''.
    """

    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end='')


if __name__ == "__main__":
    read_file("txt/my_file_0.txt")
