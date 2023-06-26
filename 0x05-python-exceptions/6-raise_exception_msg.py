#!/usr/bin/python3
# File: 6-raise_exception_msg.py
# Author: Oluwatobiloba Light


def raise_exception_msg(message=""):
    """
    Raises a name exception with a message

    Args:
        message (str, optional): Error message. Defaults to "".
    """
    raise NameError(message)
