#!/usr/bin/python3
# File: 6-print_matrix_integer.py
# Author: Oluwatobiloba Light


def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list[list[int]]): The matrix to be printed.
        Defaults to an empty matrix.

    Format:
        The matrix is printed row by row.
        Numbers are separated by a space.
        Each row is printed on a new line.

    Returns:
        None
    """
    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            print("{}".format(matrix[row][num]), end=" ")
            if num != len(matrix[row]) - 1:
                print("{}".format(matrix[row][num]), end="")
        print()
