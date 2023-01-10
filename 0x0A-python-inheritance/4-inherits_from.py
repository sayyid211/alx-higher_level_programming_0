#!/usr/binpython3
"""check indirect descendance"""


def inherits_from(obj, a_class):
    """returns indirect descendance state of obj wrt a_class"""
    return (issubclass(type(obj), a_class) and type(obj != a_class))
