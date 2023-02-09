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

    def area(self):
        """Calculates the area of the rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle instance to stdout with the character #."""
        print("\n" * self.__y +
              "\n".join([" " * self.__x + "#" * self.__width] * self.__height))

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Helper method for update."""
        self.id = id or self.id
        self.width = width or self.__width
        self.height = height or self.__height
        self.x = x or self.__x
        self.y = y or self.__y

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args:
            return self.__update(*args)
        self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle."""
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}

    def __str__(self):
        """Returns a string representation of the rectangle instance."""
        return "[{}] ({}) {}/{} - {}/{}".format(Rectangle.__name__,
                                                self.id,
                                                self.__x,
                                                self.__y,
                                                self.__width,
                                                self.__height)
