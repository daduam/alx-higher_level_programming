#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines tests for max_integer"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_max_integer(self):
        self.assertEquals(max_integer([1, 2, 3, 4]), 4)
        self.assertEquals(max_integer([2, 3, 4, 1]), 4)
        self.assertEquals(max_integer([2, 3, -4, 1]), 3)
        self.assertEquals(max_integer([-2, -3, -4, -1]), -1)
        self.assertEquals(max_integer([0, -1]), 0)
        self.assertEquals(max_integer([0], 0))


if __name__ == "__main__":
    unittest.main()
