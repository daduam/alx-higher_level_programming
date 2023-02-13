#!/usr/bin/python3
"""Test Rectangle"""

import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defines unit tests for Rectangle class."""

    def test_rectangle_inherits_from_base(self):
        """Test Rectangle inherits from Base."""
        self.assertTrue(issubclass(Rectangle, Base))


if __name__ == "__main__":
    unittest.main()
