#!/usr/bin/python3
# File: 2-append_write.py
# Author: Oluwatobiloba Light
"""Defines a function to append a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)


if __name__ == "__main__":
    nb_characters_added = append_write(
        "txt/file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
