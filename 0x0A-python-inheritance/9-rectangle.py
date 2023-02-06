#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle

        Returns:
            A string representing the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
