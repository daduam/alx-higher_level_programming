#!/usr/bin/python3
"""MagicClass module"""
import math


class MagicClass:
    """Defines magic class"""

    def __init__(self, radius):
        """
        Initializes a magic class instance.

        Args:
            radius (int|float): Radius of the circle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """
        Calculates the area of a circle.

        Returns:
            The area of a circle.
        """
        return (self.__radius**2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of a circle.

        Returns:
            The circumference of a circle.
        """
        return 2 * math.pi * self.__radius
