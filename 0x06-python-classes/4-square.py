#!/usr/bin/python3
# Author: Adamu Muhammad
"""Define square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initialize square
        Args: size - of the aquare
        Raises:
            TypeError: size !int
            ValurError: size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """fetch square size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not instanceof(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """compute square area
        Returns: area of square
        """
        area = self.__size * self.__size
        return (area)
