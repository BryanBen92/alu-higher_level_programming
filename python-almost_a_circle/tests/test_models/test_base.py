#!/usr/bin/python3
"""Test object IDs and JSON persistence for both shapes."""

from contextlib import contextmanager
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


@contextmanager
def temporary_working_directory():
    """Run file tests in an isolated directory and restore the original."""
    original = Path.cwd()
    with TemporaryDirectory() as directory:
        os.chdir(directory)
        try:
            yield
        finally:
            os.chdir(original)


class TestBase(unittest.TestCase):
    """Exercise identifier assignment and persistence operations."""

    def test_ids(self):
        first = Base()
        self.assertEqual(Base(55).id, 55)
        self.assertEqual(Base(0).id, 0)
        second = Base()
        self.assertEqual(second.id, first.id + 1)
        self.assertEqual(Rectangle(2, 3).id, second.id + 1)

    def test_json_encoding(self):
        values = [{"id": 5, "width": 2}]
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(json.loads(Base.to_json_string(values)), values)

    def test_json_decoding(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 5}]'), [{"id": 5}])

    def test_create_shapes(self):
        for source in (Rectangle(2, 3, 1, 4, 45), Square(3, 2, 1, 46)):
            with self.subTest(shape=type(source).__name__):
                details = source.to_dictionary()
                result = type(source).create(**details)
                self.assertIsNot(result, source)
                self.assertIsInstance(result, type(source))
                self.assertEqual(result.to_dictionary(), details)

    def test_save_and_load(self):
        shapes = [Rectangle(3, 4, id=31), Rectangle(2, 8, 1, 2, 32)]
        square = Square(4, 2, 3, 62)
        with temporary_working_directory():
            self.assertEqual(Rectangle.load_from_file(), [])
            self.assertEqual(Square.load_from_file(), [])
            Rectangle.save_to_file(shapes)
            Square.save_to_file([square])
            expected = [shape.to_dictionary() for shape in shapes]
            self.assertEqual(json.loads(Path("Rectangle.json").read_text()),
                             expected)
            self.assertEqual([x.to_dictionary()
                              for x in Rectangle.load_from_file()], expected)
            self.assertEqual(Square.load_from_file()[0].to_dictionary(),
                             square.to_dictionary())
            Rectangle.save_to_file(None)
            Square.save_to_file([])
            self.assertEqual(Path("Rectangle.json").read_text(), "[]")
            self.assertEqual(Path("Square.json").read_text(), "[]")
            self.assertEqual(Rectangle.load_from_file(), [])
