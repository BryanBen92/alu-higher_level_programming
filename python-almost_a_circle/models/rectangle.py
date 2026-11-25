#!/usr/bin/python3
"""Define a rectangle with validated dimensions and offsets."""

from models.base import Base


class Rectangle(Base):
    """Represent a drawable rectangle and its position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle from dimensions, offsets, and an ID."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate and set the rectangle's width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate and set the rectangle's height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the horizontal offset."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validate and set the horizontal offset."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the vertical offset."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validate and set the vertical offset."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print a rectangle of hash marks at the specified offsets."""
        print("\n" * self.y, end="")
        row = " " * self.x + "#" * self.width
        for _ in range(self.height):
            print(row)

    def __str__(self):
        """Describe the rectangle, its offsets, and its dimensions."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Update attributes, giving positional arguments priority."""
        keys = ("id", "width", "height", "x", "y")
        attributes = zip(keys, args) if args else kwargs.items()
        for key, value in attributes:
            setattr(self, key, value)

    def to_dictionary(self):
        """Return a new dictionary containing the rectangle's attributes."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
