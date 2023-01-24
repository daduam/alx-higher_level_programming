#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a size.

        Args:
            size (:obj:`int`, optional): Size of the square.
            position (:obj:`(int,int)`, optional): Coordinates of a square.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the current square area.

        Returns:
            The current square area.
        """
        return self.__size**2

    @property
    def size(self):
        """Getter for size.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print an ascii representation of the square to stdout"""
        print(self)

    @property
    def position(self):
        """
        Getter for position.

        Returns:
            The coordinates of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or type(value[0]) != int
            or type(value[1]) != int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """String representation of a square"""
        result = ""
        for y in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            for x in range(self.__position[0]):
                result += " "
            for j in range(self.__size):
                result += "#"
            result += "\n"
        return result[:-1]
