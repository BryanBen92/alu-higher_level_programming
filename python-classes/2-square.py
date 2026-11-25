#!/usr/bin/python3
"""Provide a square class for this exercise."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square with the given side length."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
