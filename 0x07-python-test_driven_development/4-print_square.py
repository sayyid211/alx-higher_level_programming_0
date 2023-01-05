#!/usr/bin/python3
"""Module for square printing"""


def print_square(size):
    """print a square of length, size """
    errors = {
        "int": "size must be an integer",
        "zero": "size must be >= 0"
        }

    if type(size) is not int:
        raise TypeError(errors["int"])
    if size < 0:
        raise ValueError(errors["zero"])
    for i in range(size):
        print('#' * size)
