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
