#!/usr/bin/python3
# File: 6-peak.py
# Author: Oluwatobiloba Light
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    length = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        length = length // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if length // 2 == 0:
                length = 2
            mid = mid + length // 2
        elif length > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if length // 2 == 0:
                length = 2
            mid = mid - length // 2
        else:
            return list_of_integers[mid]
