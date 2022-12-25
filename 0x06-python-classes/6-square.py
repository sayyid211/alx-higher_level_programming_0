#!/usr/bin/python3
"""define square class"""


class Square:
    """the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a square
        Args:
              size: Length of the square
              position: coordinates of the square
        """

        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """The size property of square
        Raises:
              TypeError: size !int
              ValueError: size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """coordinates of square properties
            Raises:
                  TypeError: if value !tuple || < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets square's position
            Args: value - a tuple of 2 ints > 0
            Raises:
                  TypeError: if value !tuple || < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """compute area of square
            Returns: area of square size **2
        """
        return (self.__size ** 2)

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos += "\n"
        for i in range(self.size):
            for p in range(self.position[0]):
                pos += " "
            for q in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end="")
