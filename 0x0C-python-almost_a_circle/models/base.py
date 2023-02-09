#!/usr/bin/python3
"""Base Model"""


class Base:
    """Defines the base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base model"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
