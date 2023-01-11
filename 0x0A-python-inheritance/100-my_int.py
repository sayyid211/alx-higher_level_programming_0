#!/usr/bin/python3
"""module my_int task"""


class MyInt(int):
    """rabel int child class"""

    def __eq__(self, other):
        """override == opr"""
        return not (self is not other)

    def __ne__(self, other):
        """override != opr"""
        return (self is not other)
