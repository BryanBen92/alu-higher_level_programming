#!/usr/bin/python3
"""Provide a square class for this exercise."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with the given side length."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the horizontal and vertical offsets."""
        return self.__position

    @position.setter
    def position(self, value):
        """Store a pair of non-negative integer offsets."""
        if (not isinstance(value, tuple) or len(value) != 2
                or any(type(item) is not int or item < 0
                       for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square in square units."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using hash characters."""
        if self.__size == 0:
            print()
            return
        horizontal, vertical = self.__position
        for _ in range(vertical):
            print()
        for _ in range(self.__size):
            print(" " * horizontal + "#" * self.__size)
