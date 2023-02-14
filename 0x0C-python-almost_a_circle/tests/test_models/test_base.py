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
        b1 = Base()
        self.assertEqual(str(type((b1))), "<class 'models.base.Base'>")

    def test_Base__nb_objects(self):
        """Checks if __nb_objects attribute is present and initialized."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)

    def test_Base__init__(self):
        """Unit tests for Base constructor."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 25)
        self.assertDictEqual(self.b1.__dict__, {'id': 1})
