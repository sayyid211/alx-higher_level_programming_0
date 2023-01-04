#!/usr/bin/python3
"""Int addition module"""


def add_integer(a, b=98):
    """Int addition function"""
    type_a, type_b = type(a), type(b)
    if type_a is not int and type_a is not float:
        raise TypeError("a must be an integer")
    if type_b is not int and type_b is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
