#!/usr/bin/python3
"""Base Model"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
