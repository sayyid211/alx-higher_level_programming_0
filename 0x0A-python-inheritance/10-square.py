#!/usr/bin/python3
"""nested inheritance module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """child of rectangle"""

    def __init__(self, size):
        """constructor"""

        self.integer_validator('size', size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
