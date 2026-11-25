#!/usr/bin/python3
"""Define a square as a specialized rectangle."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a rectangle with four equal sides."""

    def __init__(self, size):
        """Validate and store the side length."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the square's area."""
        return self.__size ** 2

    def __str__(self):
        """Return a string showing the equal square dimensions."""
        return f"[Square] {self.__size}/{self.__size}"
