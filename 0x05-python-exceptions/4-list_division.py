#!/usr/bin/python3
# File: 4-list_division.py
# Author: Oluwatobiloba Light


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides corresponding elements of two input lists and returns a new list
    of the results.

    Args:
        my_list_1 (list): The first input list.
        my_list_2 (list): The second input list.
        list_length (int): The number of elements to consider in the lists.

    Returns:
        list: A new list containing the division results of corresponding
              elements.
    """
    new_list = []
    try:
        for index in range(list_length):
            try:
                if type(my_list_1[index]) == int or type(my_list_2[index] == int):
                    new_list.append(my_list_1[index] / my_list_2[index])
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except IndexError:
                new_list.append(0)    
                print("out of range")
    finally:
       return new_list
                
    