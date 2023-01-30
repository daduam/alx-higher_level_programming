#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes rectangle with width and height

        Args:
            width (:obj:`int`, optional): Width of rectangle. Defaults to 0.
            height (:obj:`int`, optional): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): New value for width

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is negative.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): New value for height

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is negative.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of the rectangle.

        Returns:
            The rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimter of the rectangle.

        Returns:
            The rectangle perimeter or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the rectangle using #s

        Returns:
            A string representing the rectangle.
        """
        return (("#" * self.__width + "\n") * self.__height).rstrip()

    def __repr__(self):
        """Returns the canonical string representation of the object."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
