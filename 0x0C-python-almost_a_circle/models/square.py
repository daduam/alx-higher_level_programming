#!/usr/bin/python3
"""Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Helper method for update."""
        self.id = id or self.id
        self.size = size or self.size
        self.x = x or self.x
        self.y = y or self.y

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args:
            return self.__update(*args)
        self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of a Square."""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """Returns a string representation of the square instance."""
        return "[{}] ({}) {}/{} - {}".format(Square.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)
