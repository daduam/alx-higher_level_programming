#!/usr/bin/python3
"""Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """
        Initializes a square with size

        Args:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square

        Returns:
            Area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """String representation of the square.

        Returns:
            A string representing the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
