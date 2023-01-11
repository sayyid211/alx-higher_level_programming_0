#!/usr/bin/python3
"""nested inheritance module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """child of rectangle"""

    def __init__(self, size):
        """class constructor"""
        self.integer_validator('size', size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        """computes square area"""
        return (self.__size ** 2)

    def __str__(self):
        """atring representation of square"""
        return ('[Square] {}/{}'.format(self.__size, self.__size))
