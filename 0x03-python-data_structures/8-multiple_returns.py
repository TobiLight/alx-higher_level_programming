#!/usr/bin/python
# File: 8-multiple_returns.py
# Author: Oluwatobiloba Light


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string
    and its first character.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple containing two elements:
            - The length of the sentence (int).
            - The first character of the sentence (str) or
              None if the sentence is empty.
    """
    if len(sentence) == 0:
        return (len(sentence), None)
    return (len(sentence), sentence[0])
