#!/usr/bin/python3
"""define a square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """initialize square
        Args:
            size: the length of the square
        Raises:
            TypeError: size !int
            ValueErroe: size < 0
        """
        if not isinstance(size, int):
            raise Typeerror('size must be integer')
        if size < 0:
            raise ValueError('sixe must be >= 0')
        self.__size = size

    @property
    def size(self):
        """fetch square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for square size
            Args:
            value: value to give size
        Raises:
            TypeError: value not int
            ValueError: value below 0
        """
        if not isinstance(value, int):
            raise TypeError('value must be integer')
        if value < 0:
            raise ValueError('value must be >= 0')
        self.__size = value

    def area(self):
        """compute sqr area
           Returns: size ** 2
        """
        return (self.__size ** 2)

    def my_print(self):
        """print square with #"""
        if self.size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
