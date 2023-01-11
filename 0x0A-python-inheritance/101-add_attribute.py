#!/usr/bin/python3
"""add attribute module"""


def add_attribute(obj, name, value):
    """add or modify an object's attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
