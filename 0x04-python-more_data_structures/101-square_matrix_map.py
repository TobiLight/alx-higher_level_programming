#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return ([map(lambda x: [map(lambda y: y ** 2, x[:])], matrix)])