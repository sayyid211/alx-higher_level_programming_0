#!/usr/bin/python3
"""module subclass rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """descendant of basegeometry"""

    def __init__(self, width, height):
        """class constructor"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """compute rectangle's area"""
        return (self.__width * self.__height)

    def __str__(self):
        """return rectangle's string representation"""
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
