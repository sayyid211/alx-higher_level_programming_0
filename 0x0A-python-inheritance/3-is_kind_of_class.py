#!/usr/bin/python3
"""check if object is a descendant of another"""


def is_kind_of_class(obj, a_class):
    """return descendance state of obj wrt a_class"""

    return (isinstance(obj, a_class))
