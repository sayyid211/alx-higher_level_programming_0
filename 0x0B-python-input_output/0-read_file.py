#!/usr/bin/python3
"""Module to read file """


def read_file(filename=""):
    """Read a file and display the contents to stdout"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
