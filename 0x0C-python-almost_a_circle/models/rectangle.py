#!/usr/bin/python3
"""Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__validate_dimen("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__validate_dimen("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__validate_dimen("x", value, excludes_zero=False)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__validate_dimen("y", value, excludes_zero=False)
        self.__y = value

    def __validate_dimen(self, name, value, excludes_zero=True):
        """Validates dimensions"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if excludes_zero and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not excludes_zero and value < 0:
            raise ValueError("{} must be >= 0".format(name))
