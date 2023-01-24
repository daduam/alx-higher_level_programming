#!/usr/bin/python3
class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize the square with a size.

        Args:
            size (:obj:`int`, optional): Size of the square.
        """
        self.__size = size

    def area(self):
        """Calculates the current square area.

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
