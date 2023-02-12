#!/usr/bin/python3
"""Base Model"""


import json
import os
import csv


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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of cls from file."""
        filename = "{}.json".format(cls.__name__)
        instances = []
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                for dictionary in cls.from_json_string(f.read()):
                    instances.append(cls.create(**dictionary))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instances to a csv file."""
        list_dictionaries, fieldnames = [], []
        if list_objs:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            fieldnames = ['id', 'size', 'x', 'y']
        with open("{}.csv".format(cls.__name__), "w") as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_dictionaries)

    @classmethod
    def load_from_file_csv(cls):
        """Loads instances from a csv file."""
        filename = "{}.csv".format(cls.__name__)
        instances, fieldnames = [], []
        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            fieldnames = ['id', 'size', 'x', 'y']
        if os.path.isfile(filename):
            with open(filename, "r") as csvf:
                reader = csv.DictReader(csvf)
                for row in reader:
                    dictionary = {}
                    for key in fieldnames:
                        dictionary[key] = int(row[key])
                    instances.append(cls.create(**dictionary))
        return instances
