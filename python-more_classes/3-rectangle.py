#!/usr/bin/python3
"""Define a rectangle and its geometric operations."""


class Rectangle:
    """Represent a rectangle with a width and a height."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with validated dimensions."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate and set the rectangle's width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate and set the rectangle's height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter, or zero for an empty rectangle."""
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Draw the rectangle using its print symbol."""
        if not self.__width or not self.__height:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)
