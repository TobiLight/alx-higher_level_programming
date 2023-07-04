#!/usr/bin/python3
# File: 101-matrix_mul.py
# Author: Oluwatobiloba Light
"""Multiply two matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a
                list of lists,
                   or if one element of the matrices is not an integer
                   or a float,
                   or if each row of m_a or m_b is not of the same size.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be
                multiplied.

    Returns:
        list: The resulting matrix after multiplication.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or\
            not all(isinstance(row, list) for row in m_b):
        raise TypeError(
            "m_a must be a list of lists or m_b must be a list of lists")

    if m_a == [] or m_b == [] or any(row == [] for row in m_a) or\
            any(row == [] for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if any(not isinstance(element, (int, float))
           for row in m_a for element in row) or\
            any(not isinstance(element, (int, float))
                for row in m_b for element in row):
        raise TypeError(
            "m_a should contain only integers or floats or m_b should\
                contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1 or\
            len(set(len(row) for row in m_b)) > 1:
        raise TypeError(
            "each row of m_a must be of the same size or each row of m_b must\
                be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
