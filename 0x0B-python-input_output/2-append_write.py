#!/usr/bin/python3
"""Module to append text to file"""


def append_write(filename="", text=""):
    """appends text to file"""
    with open(filename, 'a') as f:
        return (f.write(text))
