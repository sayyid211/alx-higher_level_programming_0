#!/usr/bin/python3
"""Module for file writing"""


def write_file(filename="", text=""):
    """Override the content of a text file"""
    with open(filename, 'w') as f:
        return(f.write(text))
