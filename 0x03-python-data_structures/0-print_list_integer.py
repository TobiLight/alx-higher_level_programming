#!/usr/bin/python3
# File: 0-print_list_integer.py
# Author: Oluwatobiloba Light


def print_list_integer(mylist=[]):
    """Prints integers of a list"""
    for item in range(len(mylist)):
        print("{:d}".format(mylist[item]))
