#!/usr/bin/python3
"""Define the base geometry class."""


class BaseGeometry:
    """Provide a base for geometric shapes."""

    def area(self):
        """Require a subclass to implement area calculation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a named value is a strictly positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
