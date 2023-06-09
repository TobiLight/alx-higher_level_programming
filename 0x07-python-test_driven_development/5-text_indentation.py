#!/usr/bin/python3
# File: 5-text_indentation.py
# Author: Oluwatobiloba Light
"""Prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Prints a text with modified identation

    Args:
        text (str): The input text to be processed and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    string = ''
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] in '.?:' or text[i] == '\n':
            if text[i] in '.?:':
                print('\n')
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
