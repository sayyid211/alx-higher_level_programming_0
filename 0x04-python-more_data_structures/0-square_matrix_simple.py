#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return([list(map(lambda i: i * i, x)) for x in matrix])
