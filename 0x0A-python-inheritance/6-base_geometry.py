#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Defines base geometry"""

    def area(self):
        """Calculates the area of the geometry"""
        raise Exception("area() is not implemented")
