#!/usr/bin/python3
"""Test Base"""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Defines unit tests for Base class."""

    def test_Base__nb_objects(self):
        """Checks if __nb_objects attribute is present and initialized."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)


if __name__ == "__main__":
    unittest.main()
