#!/usr/bin/python3
"""Define the base geometry class."""


class BaseGeometry:
    """Provide a base for geometric shapes."""

    def area(self):
        """Require a subclass to implement area calculation."""
        raise Exception("area() is not implemented")
