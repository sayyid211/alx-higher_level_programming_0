#!/usr/bin/python3
"""module subclass rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle descendant of basegeometry"""

    def __init__(self, width, height):
        """class constructor"""

        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
