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

    def test_from_json_string_static_method(self):
        """Test from_json_string static method."""
        self.assertIn("from_json_string", dir(Base))

        result = Base.from_json_string(None)
        self.assertEqual(result, [])

        result = Base.from_json_string("")
        self.assertEqual(result, [])

        expected = [{"x": 1, "y": 2},
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7},
                    {"x": 1, "y": 2, "width": 3, "height": 4}]
        json_string = Base.to_json_string(expected)
        result = Base.from_json_string(json_string)
        for i in range(len(expected)):
            self.assertDictEqual(expected[i], result[i])

    def test_create_class_method(self):
        """Test create class method."""
        self.assertIn("create", dir(Base))

        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertDictEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)
        self.assertTrue(r1 is not r2)

        sq1 = Square(3, 5, 1)
        sq2 = Square.create(**sq1.to_dictionary())
        self.assertDictEqual(sq1.to_dictionary(), sq2.to_dictionary())
        self.assertEqual(str(sq1), str(sq2))
        self.assertNotEqual(sq1, sq2)
        self.assertTrue(sq1 is not sq2)

    def test_load_from_file_class_method(self):
        """Test load_from_file class method."""
        self.assertIn("load_from_file", dir(Base))

        rectangle_json_filename = "Rectangle.json"
        square_json_filename = "Square.json"

        if os.path.exists(rectangle_json_filename):
            os.remove(rectangle_json_filename)

        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

        if os.path.exists(square_json_filename):
            os.remove(square_json_filename)

        result = Square.load_from_file()
        self.assertEqual(result, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        expected = [r1, r2]
        Rectangle.save_to_file(expected)
        result = Rectangle.load_from_file()
        for i in range(len(expected)):
            self.assertEqual(str(expected[i]), str(result[i]))

        sq1 = Square(5)
        sq2 = Square(7, 9, 1)
        expected = [sq1, sq2]
        Square.save_to_file(expected)
        result = Square.load_from_file()
        for i in range(len(expected)):
            self.assertEqual(str(expected[i]), str(result[i]))
