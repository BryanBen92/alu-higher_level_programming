#!/usr/bin/python3
"""Provide a square class for this exercise."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square with the given side length."""
        self.size = size

    @property
    def size(self):
        """Return the length of a side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the length of a side after validating it."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square in square units."""
        return self.__size ** 2
