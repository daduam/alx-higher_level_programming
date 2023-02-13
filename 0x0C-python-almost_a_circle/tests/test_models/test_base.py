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

    def test_Base__nb_objects(self):
        """Checks if __nb_objects attribute is present and initialized."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)

    def test_Base__init__(self):
        """Unit tests for Base constructor."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 25)


if __name__ == "__main__":
    unittest.main()
