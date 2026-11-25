#!/usr/bin/python3
"""Add two numbers after converting each to an integer."""


def add_integer(a, b=98):
    """Return the sum of two individually truncated numbers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
