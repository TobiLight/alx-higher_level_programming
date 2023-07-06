#!/usr/bin/python3
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
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix1 = []
    for x in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][x])
        matrix1.append(new_row)

    result = []
    for row in m_a:
        matrix2 = []
        for col in matrix1:
            product = 0
            for i in range(len(matrix1[0])):
                product += row[i] * col[i]
            matrix2.append(product)
        result.append(matrix2)

    return result
