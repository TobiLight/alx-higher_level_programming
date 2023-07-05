#!/usr/bin/python3
# File: 2-matrix_divided.py
# Author: Oluwatobiloba Light
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide each element of a matrix by a given number.

    Args:
        matrix (list): The matrix to be divided, a list of lists.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new list of the resulting matrix after division.

    Raises:
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If the matrix contains non-numbers.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If the division by zero is attempted.
    """
    if (
        not isinstance(matrix, list)
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            isinstance(ele, int) or isinstance(ele, float)
            for ele in [num for row in matrix for num in row]
        )
        or matrix == []
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
