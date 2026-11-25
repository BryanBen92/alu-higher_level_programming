#!/usr/bin/python3
"""Define a square using the rectangle model."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a rectangle with equal dimensions."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize equal sides and apply the given position and ID."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Describe the square, its position, and its side length."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Return the length of one side."""
        return self.width

    @size.setter
    def size(self, value):
        """Validate the side length and update both dimensions."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square attributes, giving positional arguments priority."""
        keys = ("id", "size", "x", "y")
        attributes = zip(keys, args) if args else kwargs.items()
        for key, value in attributes:
            setattr(self, key, value)

    def to_dictionary(self):
        """Return a new dictionary containing the square's attributes."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
