#!/usr/bin/python3
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
    # new_list = []
    # for item in my_list:
    #     if item == search:
    #         new_list.append(replace)
    #     else:
    #         new_list.append(item)
    return [replace if x == search else x for x in my_list]
