#!/usr/bin/python3
"""Test Square"""

from contextlib import redirect_stdout
import io
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

    def test_constructor_wrong_number_of_arguments(self):
        """Test Square constructor with wrong number of arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_constructor_only_size_positional_argument(self):
        """Test Square constructor with only size positional argument."""
        Base._Base__nb_objects = 0

        sq = Square(1)
        self.assertEqual(sq.width, 1)
        self.assertEqual(sq.height, 1)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, getattr(Base, "_Base__nb_objects"))

    def test_constructor_with_one_keyword_argument(self):
        """Test Square constructor with one keyword argument."""
        Base._Base__nb_objects = 0

        sq1 = Square(1, x=2)
        self.assertEqual(sq1.width, 1)
        self.assertEqual(sq1.height, 1)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq1.y, 0)
        self.assertEqual(sq1.id, getattr(Base, "_Base__nb_objects"))

        sq2 = Square(1, y=2)
        self.assertEqual(sq2.width, 1)
        self.assertEqual(sq2.height, 1)
        self.assertEqual(sq2.x, 0)
        self.assertEqual(sq2.y, 2)
        self.assertEqual(sq2.id, getattr(Base, "_Base__nb_objects"))

        sq3 = Square(1, id=25)
        self.assertEqual(sq3.width, 1)
        self.assertEqual(sq3.height, 1)
        self.assertEqual(sq3.x, 0)
        self.assertEqual(sq3.y, 0)
        self.assertEqual(sq3.id, 25)

    def test_constructor_with_two_keyword_arguments(self):
        """Test constructor with two keyword arguments."""
        Base._Base__nb_objects = 0

        sq1 = Square(1, x=2, y=3)
        self.assertEqual(sq1.width, 1)
        self.assertEqual(sq1.height, 1)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq1.y, 3)
        self.assertEqual(sq1.id, getattr(Base, "_Base__nb_objects"))

        sq2 = Square(1, x=2, id=25)
        self.assertEqual(sq2.width, 1)
        self.assertEqual(sq2.height, 1)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 0)
        self.assertEqual(sq2.id, 25)

        sq3 = Square(1, y=2, id=25)
        self.assertEqual(sq3.width, 1)
        self.assertEqual(sq3.height, 1)
        self.assertEqual(sq3.x, 0)
        self.assertEqual(sq3.y, 2)
        self.assertEqual(sq3.id, 25)

    def test_constructor_with_all_arguments(self):
        """Test constructor with all arguments."""
        sq = Square(1, x=2, y=3, id=25)
        self.assertEqual(sq.width, 1)
        self.assertEqual(sq.height, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 25)
        self.assertDictEqual(sq.__dict__, {'id': 25,
                                           '_Rectangle__width': 1,
                                           '_Rectangle__height': 1,
                                           '_Rectangle__x': 2,
                                           '_Rectangle__y': 3})

    def test_width_and_height_setter_validation(self):
        """Test width and height setter validation."""
        sq = Square(1)

        bad_values = ["1", [1], (1,), {1}, dict()]

        for value in bad_values:
            with self.assertRaisesRegex(TypeError,
                                        "width must be an integer"):
                sq.width = value
            with self.assertRaisesRegex(TypeError,
                                        "height must be an integer"):
                sq.height = value

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.width = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.width = -3

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            sq.height = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            sq.height = -3

    def test_x_and_y_setter_validation(self):
        """Test width and height setter validation."""
        sq = Square(1)

        bad_values = ["1", [1], (1,), {1}, dict()]

        for value in bad_values:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                sq.x = value
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                sq.y = value

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.x = -3

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.y = -3

    def test_area_public_method(self):
        """Test area public method."""
        self.assertIn("area", dir(Square))

        sq1 = Square(5)
        self.assertEqual(sq1.area(), 25)

        sq2 = Square(2, 2)
        self.assertEqual(sq2.area(), 4)

        sq3 = Square(3, 1, 3)
        self.assertEqual(sq3.area(), 9)

        sq4 = Square(8, 0, 0, 12)
        self.assertEqual(sq4.area(), 64)

    def test_display_public_method(self):
        """Test display public method."""
        self.assertIn("display", dir(Square))

        sq1 = Square(4)
        with redirect_stdout(io.StringIO()) as f:
            sq1.display()
        self.assertEqual(f.getvalue(), "####\n####\n####\n####\n")

        sq2 = Square(2)
        with redirect_stdout(io.StringIO()) as f:
            sq2.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

        sq3 = Square(2, 3, 2)
        with redirect_stdout(io.StringIO()) as f:
            sq3.display()
        self.assertEqual(f.getvalue(), "\n\n   ##\n   ##\n")

        sq4 = Square(3, 2, 1)
        with redirect_stdout(io.StringIO()) as f:
            sq4.display()
        self.assertEqual(f.getvalue(), "\n  ###\n  ###\n  ###\n")

    def test__str__method_override(self):
        """Test __str__ method override"""
        Base._Base__nb_objects = 0

        sq1 = Square(6, 2, 1, 12)
        self.assertEqual(sq1.__str__(), "[Square] (12) 2/1 - 6")

        sq2 = Square(5, 1)
        self.assertEqual(sq2.__str__(), "[Square] (1) 1/0 - 5")

        sq3 = Square(5)
        self.assertEqual(sq3.__str__(), "[Square] (2) 0/0 - 5")

        sq4 = Square(2, 2)
        self.assertEqual(sq4.__str__(), "[Square] (3) 2/0 - 2")

        sq5 = Square(3, 1, 3)
        self.assertEqual(sq5.__str__(), "[Square] (4) 1/3 - 3")

    def test_square_size_getter(self):
        """Test Square size getter."""
        sq = Square(1)
        self.assertEqual(sq.size, sq.width)
        self.assertEqual(sq.size, sq.height)
        self.assertEqual(sq.size, 1)

    def test_square_size_setter(self):
        """Test Square size setter"""
        sq = Square(1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.size = "13"

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.size = 0

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.size = -12

        sq.size = 34
        self.assertEqual(sq.size, 34)
        self.assertEqual(sq.size, sq.width)
        self.assertEqual(sq.size, sq.height)
