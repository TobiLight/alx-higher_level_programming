#!/usr/bin/python3
# File: 1-write_file.py
# Author: Oluwatobiloba Light
"""Defines a function to write text to file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of
    characters written

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text to write to file. Defaults to "".

    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)


if __name__ == "__main__":
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
