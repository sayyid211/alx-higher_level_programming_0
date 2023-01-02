#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """rectangle constructor"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """height getter"""
        return self.__heightx

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueErroe("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueErroe("width must be >= 0")
        self.__width = value
