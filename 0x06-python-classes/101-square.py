#!/usr/bin/python3
class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a size.

        Args:
            size (:obj:`int`, optional): Size of the square.
            position (:obj:`tuple`, optional): Coordinates of a square.
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """Print an ascii representation of the square to stdout"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Getter for position"""
        return self.position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if (
            type(value) != tuple
            or len(value) != 2
            or any(type(i) != int for i in value)
            or any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        """String representation of a square"""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for i in range(self.__size):
                result += " " * self.__position[0]
                result += "#" * self.__size
                if i != self.__size - 1:
                    result += "\n"
        return result
