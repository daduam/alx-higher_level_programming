#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Defines base geometry"""

    def area(self):
        """Calculates the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name (str): Name.
            value (int): Value.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is less than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
