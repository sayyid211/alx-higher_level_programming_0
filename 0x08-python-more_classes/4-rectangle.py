#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.height = height

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get width """
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """compute area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """compute perimeter"""
        if (self.__height == 0 or self.__width == 0):
            return (0)
        return (2 * (self.__height * self.__width))

    def __str__(self):
        """rectangle str"""
        w, h = self.__width, self.__height
        if w == 0 or h == 0:
            return ''
        return "{}{}".format(("#" * w + '\n') * (h - 1), "#" * w)

    def __repr__(self):
        """Rectangle's representation"""
        w, h = self.__width, self.__height
        return "Rectangle({}, {})".format(w, h)
