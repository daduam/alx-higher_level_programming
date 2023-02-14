#!/usr/bin/python3
"""Test Base"""

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Defines unit tests for Base class."""

    def setUp(self) -> None:
        self.b1 = Base()
        self.b2 = Base(25)
        return super().setUp()

    def test_base_in_correct_module(self):
        """Test Base in correct module."""
        self.assertEqual(str(Base), "<class 'models.base.Base'>")

    def test_Base__nb_objects(self):
        """Checks if __nb_objects attribute is present and initialized."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)

    def test_Base__init__(self):
        """Unit tests for Base constructor."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 25)
        self.assertDictEqual(self.b1.__dict__, {'id': 1})

    def test_to_json_string_static_method(self):
        """Test to_json_string static method"""
        self.assertIn("to_json_string", dir(Base))

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([]), "[]")

        list_dictionaries = [{"x": 1, "y": 2}]
        result = Base.to_json_string(list_dictionaries)
        expected = str(list_dictionaries).replace("'", '"')
        self.assertEqual(result, expected)

        list_dictionaries = [{"x": 1, "y": 2},
                             {"x": 1, "y": 2, "width": 3, "height": 4}]
        result = Base.to_json_string(list_dictionaries)
        expected = str(list_dictionaries).replace("'", '"')
        self.assertEqual(result, expected)

    def test_save_to_file_class_method(self):
        """Test save_to_file class method."""
        self.assertIn("save_to_file", dir(Base))

        rectangle_json_filename = "Rectangle.json"
        square_json_filename = "Square.json"

        Rectangle.save_to_file(None)
        with open(rectangle_json_filename, "r") as f:
            result = f.read()
        expected = "[]"
        self.assertEqual(result, expected)

        Square.save_to_file(None)
        with open(square_json_filename, "r") as f:
            result = f.read()
        expected = "[]"
        self.assertEqual(result, expected)

        sq1 = Rectangle(10, 7, 2, 8)
        sq2 = Rectangle(2, 4)
        Rectangle.save_to_file([sq1, sq2])
        with open(rectangle_json_filename, "r") as f:
            result = f.read()
        expected = Base.to_json_string(
            [sq1.to_dictionary(), sq2.to_dictionary()])
        self.assertEqual(result, expected)

        sq1 = Square(10, 7, 2)
        sq2 = Square(2)
        Square.save_to_file([sq1, sq2])
        with open(square_json_filename, "r") as f:
            result = f.read()
        expected = Base.to_json_string(
            [sq1.to_dictionary(), sq2.to_dictionary()])
        self.assertEqual(result, expected)

        if os.path.exists(rectangle_json_filename):
            os.remove(rectangle_json_filename)

        if os.path.exists(square_json_filename):
            os.remove(square_json_filename)
