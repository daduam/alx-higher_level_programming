#!/usr/bin/python3
"""Test Base"""

import unittest

from models.base import Base


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
