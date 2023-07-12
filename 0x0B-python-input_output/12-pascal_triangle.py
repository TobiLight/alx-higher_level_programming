#!/usr/bin/python3
# File:12-pascal_triangle.py
# Author: Oluwatobiloba Light
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Represents Pascal's Triangle of size n.

    Args:
        n (int): Size of triangle

    Returns:
        A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles


def print_triangle(triangle):
    """
    Prints the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
