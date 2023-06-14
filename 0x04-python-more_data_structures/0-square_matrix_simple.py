#!/usr/bin/python3
# File: 0-square_matrix_simple.py
# Author: Oluwatobiloba Light


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix (list[list]): A 2-dimensional array.

    Returns:
        list[list]: A new matrix with the same size
                    as the input matrix.
                    Each value in the new matrix is the
                    square of the corresponding value in
                    the input matrix.
    """
    square_matrix = []
    for i in range(len(matrix)):
        row_of_squares = []
        for row in range(len(matrix[i])):
            row_of_squares.append(matrix[i][row] * matrix[i][row])
        square_matrix.append(row_of_squares)
    return square_matrix_simple
