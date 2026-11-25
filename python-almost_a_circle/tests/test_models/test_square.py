#!/usr/bin/python3
"""Test square dimensions, display, and attribute updates."""

from contextlib import redirect_stdout
from io import StringIO
import unittest

from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Exercise equal sides and the square-specific interface."""

    def test_square_dimensions(self):
        square = Square(4)
        self.assertIsInstance(square, Rectangle)
        self.assertEqual((square.size, square.width, square.height), (4, 4, 4))
        square.size = 6
        self.assertEqual((square.width, square.height), (6, 6))
        self.assertEqual(square.area(), 36)

    def test_validation(self):
        square = Square(4)
        for invalid in (None, 2.5, "3", True):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(TypeError,
                                            "^width must be an integer$"):
                    square.size = invalid
        for invalid in (0, -3):
            with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
                square.size = invalid
        self.assertEqual(square.size, 4)

    def test_display_and_text(self):
        square = Square(2, 3, 1, 8)
        output = StringIO()
        with redirect_stdout(output):
            square.display()
        self.assertEqual(output.getvalue(), "\n   ##\n   ##\n")
        self.assertEqual(str(square), "[Square] (8) 3/1 - 2")

    def test_updates_and_dictionary(self):
        square = Square(2, id=10)
        square.update()
        square.update(7, 3, 1, 2, size=8)
        self.assertEqual(square.to_dictionary(),
                         {"id": 7, "size": 3, "x": 1, "y": 2})
        square.update(y=4, size=5)
        self.assertEqual(square.to_dictionary(),
                         {"id": 7, "size": 5, "x": 1, "y": 4})
        self.assertEqual(square.height, 5)
        with self.assertRaises(ValueError):
            square.update(size=-2)

    def test_constructor_defaults_with_offsets(self):
        horizontal = Square(1, 2)
        self.assertEqual((horizontal.size, horizontal.x, horizontal.y),
                         (1, 2, 0))
        both = Square(1, 2, 3)
        self.assertEqual((both.size, both.width, both.height), (1, 1, 1))
        self.assertEqual((both.x, both.y), (2, 3))

    def test_constructor_rejects_invalid_types(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_constructor_rejects_invalid_values(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)
