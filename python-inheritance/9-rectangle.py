#!/usr/bin/python3
"""Define a rectangle with validated dimensions."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with positive dimensions."""

    def __init__(self, width, height):
        """Validate and store the width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string showing the rectangle dimensions."""
        return f"[Rectangle] {self.__width}/{self.__height}"
