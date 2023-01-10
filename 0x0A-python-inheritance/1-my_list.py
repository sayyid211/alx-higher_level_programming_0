#!/usr/bin/python3
"""Define a class that is child to another"""


class MyList(list):
    """Subclass of list"""

    def print_sorted(self):
        """print a list sorted in ascending order"""
        print(sorted(self))
