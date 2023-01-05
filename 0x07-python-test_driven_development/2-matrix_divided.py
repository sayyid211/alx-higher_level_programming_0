#!/usr/bin/python3
"""matrix division module"""


def matrix_divided(matrix, div):
    """divides matrix by div"""

    errors = {
        "matrix": "matrix must be a matrix (list of lists) of integers/floats",
        "row": "Each row of the matrix must have the same size",
        "div": "div must be a number",
        "zero": "division by zero"
        }

    if type(matrix) is not list:
        raise TypeError(errors['matrix'])

    row_size = None
    for row in matrix:
        """check if is list"""
        if type(row) is not list:
            raise TypeError(errors['matrix'])

        """check size of rows"""
        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError(errors['row'])

        """check that all items are valid numbers (int/float)"""
        status = all(type(element) in set([int, float]) for element in row)
        if status is False:
            raise TypeError(errors['matrix'])

    if type(div) not in [int, float]:
        raise TypeError(errprs['div'])

    if div == 0:
        raise ZeroDivisionError(errors['zero'])

    new = map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)
    return list(new)
