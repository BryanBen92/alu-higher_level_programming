#!/usr/bin/python3
"""Test the maximum-element exercise against representative sequences."""

import unittest


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Exercise empty, ordered, and mixed numeric input."""

    def test_empty(self):
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_maximum_positions(self):
        self.assertEqual(max_integer([9, 2, 3]), 9)
        self.assertEqual(max_integer([1, 9, 3]), 9)
        self.assertEqual(max_integer([1, 2, 9]), 9)

    def test_duplicates_and_negative_values(self):
        self.assertEqual(max_integer([8, 8, 3, 8]), 8)
        self.assertEqual(max_integer([-9, -2, -5]), -2)
        self.assertEqual(max_integer([-5, 0, -1]), 0)

    def test_floating_and_mixed_numbers(self):
        self.assertEqual(max_integer([1.2, 2.3, 1.1]), 2.3)
        self.assertEqual(max_integer([2, 3.5, -1]), 3.5)

    def test_comparable_strings(self):
        self.assertEqual(max_integer(["ant", "zebra", "bear"]), "zebra")
        self.assertEqual(max_integer("abc"), "c")
        self.assertIsNone(max_integer(""))

    def test_preserves_input(self):
        values = [3, 2, 4]
        self.assertEqual(max_integer(values), 4)
        self.assertEqual(values, [3, 2, 4])
