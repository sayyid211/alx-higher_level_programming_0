#!/usr/bin/python3
"""Define square class"""


class Square:
    """the square class"""

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

    def area(self):
        """compute square area
        Returns: area of square
        """
        area = self.__size * self.__size
        return (area)
