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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        list_dictionaries = []
        if list_objs:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of cls with attributes from dictionary."""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
