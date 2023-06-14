#!/usr/bin/pyhton3
# File: 1-search_replace.py
# Author: Oluwatobiloba Light


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element with
    another element in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        list: A new list with all occurrences of the
        search element replaced by the replace element.
    """
    my_list_cpy = []
    for i in range(len(my_list)):
        my_list_cpy[i] = my_list[i]
        if my_list[i] == search:
            my_list_cpy[i] = replace
    return my_list_cpy
