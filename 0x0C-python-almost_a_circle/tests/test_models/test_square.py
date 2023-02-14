#!/usr/bin/python3
"""Test Square"""

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Defines unit tests for Square class."""

    def test_square_in_correct_module(self):
        """Test Square in correct module."""
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_square_inheritance(self):
        """Test Square inheritance"""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_private_instance_attributes(self):
        """Test private instance attributes."""
        sq = Square(1)
        self.assertTrue(hasattr(sq, "_Rectangle__width"))
        self.assertTrue(hasattr(sq, "_Rectangle__height"))
        self.assertTrue(hasattr(sq, "_Rectangle__x"))
        self.assertTrue(hasattr(sq, "_Rectangle__y"))

    def test_private_instance_attributes_getters(self):
        """Test private instance attributes getters."""
        sq = Square(1)
        self.assertEqual(sq.width, 1)
        self.assertEqual(sq.height, 1)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)

    def test_private_instance_attributes_setters(self):
        """Test private instance attributes setters."""
        sq = Square(1)
        sq.width = 2
        sq.height = 2
        sq.x = 3
        sq.y = 4
        self.assertEqual(sq.width, 2)
        self.assertEqual(sq.height, 2)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)
