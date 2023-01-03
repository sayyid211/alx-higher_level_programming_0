#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """new rectangle class"""

    def init(self, width=0, height=0):
        """constructor"""
        self.__height = height
        self.width = width

    @property
    def width(self):
        """get width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width"""
        if value is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """compute area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """compute perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """rectangle str"""
        l, b = self.__width, self.__height
        if l == 0 or b == 0:
            return ('')
        return ('{}{}'.format(('#' * l + '\n') * (b - 1), '#' * l))
