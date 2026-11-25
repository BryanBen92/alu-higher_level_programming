#!/usr/bin/python3
"""Test rectangle properties, presentation, and updates."""

from contextlib import redirect_stdout
from io import StringIO
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Exercise rectangle behavior and exact validation messages."""

    def test_dimensions_and_inheritance(self):
        rectangle = Rectangle(4, 5)
        self.assertIsInstance(rectangle, Base)
        self.assertEqual((rectangle.width, rectangle.height), (4, 5))
        self.assertEqual((rectangle.x, rectangle.y), (0, 0))
        rectangle.width, rectangle.height = 3, 2
        rectangle.x, rectangle.y = 4, 1
        self.assertEqual((rectangle.width, rectangle.height), (3, 2))
        self.assertEqual((rectangle.x, rectangle.y), (4, 1))
        self.assertEqual(rectangle.area(), 6)

    def test_validation(self):
        rectangle = Rectangle(4, 5)
        for key in ("width", "height", "x", "y"):
            for invalid in (1.5, True, None, "4", [], {}):
                with self.subTest(key=key, invalid=invalid):
                    with self.assertRaisesRegex(
                            TypeError, f"^{key} must be an integer$"):
                        setattr(rectangle, key, invalid)
            symbol = ">" if key in ("width", "height") else ">="
            with self.assertRaisesRegex(ValueError,
                                        f"^{key} must be {symbol} 0$"):
                setattr(rectangle, key, -1)
        for key in ("width", "height"):
            with self.assertRaises(ValueError):
                setattr(rectangle, key, 0)
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            Rectangle("2", 4)

    def test_display_and_text(self):
        rectangle = Rectangle(2, 3, 1, 2, 18)
        output = StringIO()
        with redirect_stdout(output):
            rectangle.display()
        self.assertEqual(output.getvalue(), "\n\n ##\n ##\n ##\n")
        self.assertEqual(str(rectangle), "[Rectangle] (18) 1/2 - 2/3")

    def test_update_and_dictionary(self):
        rectangle = Rectangle(2, 3, id=11)
        rectangle.update()
        rectangle.update(21, 4, 5, 6, 7, width=8)
        expected = {"id": 21, "width": 4, "height": 5, "x": 6, "y": 7}
        self.assertEqual(rectangle.to_dictionary(), expected)
        rectangle.update(height=9, id=30)
        expected.update(height=9, id=30)
        self.assertEqual(rectangle.to_dictionary(), expected)
        detached = rectangle.to_dictionary()
        detached["width"] = 99
        self.assertEqual(rectangle.width, 4)
        with self.assertRaises(ValueError):
            rectangle.update(width=0)
