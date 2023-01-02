#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
        """rectangle class"""
        def __init__(self, width=0, height=0):
            """rectangle constructor"""
            self.__width = width
            self.__height = height

        @property
        def height(self):
            """height getter"""
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
                """get width"""
                return self.__width

        @width.setter
        def width(self):
                """set width"""
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                self.__width = value

        def area(self):
                """area of rectangle"""
                return self.__height * self.__width

        def perimeter(self):
                return (2 * (self.__height + self.width))
