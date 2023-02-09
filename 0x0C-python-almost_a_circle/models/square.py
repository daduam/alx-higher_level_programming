#!/usr/bin/python3
"""Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square instance."""
        return "[{}] ({}) {}/{} - {}".format(Square.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)
