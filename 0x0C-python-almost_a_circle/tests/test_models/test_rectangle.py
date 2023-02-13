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

    def test_private_instance_attributes(self):
        """Test private instance attributes."""
        r1 = Rectangle(1, 1)
        self.assertTrue(hasattr(r1, "_Rectangle__width"))
        self.assertTrue(hasattr(r1, "_Rectangle__height"))
        self.assertTrue(hasattr(r1, "_Rectangle__x"))
        self.assertTrue(hasattr(r1, "_Rectangle__y"))

    def test_private_instance_attributes_getters(self):
        """Test private instance attributes getters."""
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_private_instance_attributes_setters(self):
        """Test private instance attributes setters."""
        r1 = Rectangle(2, 3)
        r1.width = 5
        r1.height = 7
        r1.x = 2
        r1.y = 3
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)

    def test_constructor_wrong_number_of_arguments(self):
        """Test rectangle constructor with wrong number of arguments"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_constructor_only_positional_arguments(self):
        """Test rectangle constructor with only positional arguments."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, getattr(Base, "_Base__nb_objects"))

    def test_constructor_with_one_keyword_argument(self):
        """Test rectangle constructor with one keyword argument."""
        r1 = Rectangle(1, 2, x=3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, getattr(Base, "_Base__nb_objects"))

        r2 = Rectangle(1, 2, y=3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, getattr(Base, "_Base__nb_objects"))

        r3 = Rectangle(1, 2, id=25)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 25)

    def test_constructor_with_two_keyword_arguments(self):
        """Test constructor with two keyword arguments."""
        r1 = Rectangle(1, 2, x=3, y=4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, getattr(Base, "_Base__nb_objects"))

        r2 = Rectangle(1, 2, x=3, id=25)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 25)

        r3 = Rectangle(1, 2, y=3, id=25)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 3)
        self.assertEqual(r3.id, 25)

    def test_constructor_with_all_arguments(self):
        """Test constructor with all arguments."""
        r1 = Rectangle(1, 2, x=3, y=4, id=25)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 25)
        self.assertDictEqual(r1.__dict__, {'id': 25,
                                           '_Rectangle__width': 1,
                                           '_Rectangle__height': 2,
                                           '_Rectangle__x': 3,
                                           '_Rectangle__y': 4})

    def test_width_and_height_setter_validation(self):
        """Test width and height setter validation."""
        r1 = Rectangle(1, 2)

        bad_values = ["1", [1], (1,), {1}, dict()]

        for value in bad_values:
            with self.assertRaisesRegex(TypeError,
                                        "width must be an integer"):
                r1.width = value
            with self.assertRaisesRegex(TypeError,
                                        "height must be an integer"):
                r1.height = value

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = -3

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.height = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.height = -3

    def test_x_and_y_setter_validation(self):
        """Test width and height setter validation."""
        r1 = Rectangle(1, 2)

        bad_values = ["1", [1], (1,), {1}, dict()]

        for value in bad_values:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                r1.x = value
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                r1.y = value

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.x = -3

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.y = -3

    def test_area_public_method(self):
        """Test area public method."""
        self.assertIn('area', dir(Rectangle))

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
