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
        sq = Square(1)
        self.assertEqual(str(type((sq))), "<class 'models.square.Square'>")
