#!/usr/bin/python3
# File:100-append_after.py
# Author: Oluwatobiloba Light
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as my_file2:
        my_file2.write(text)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
