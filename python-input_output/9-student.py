#!/usr/bin/python3
"""Serialize student information."""


class Student:
    """Store identifying information for a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the student's attributes as a dictionary."""
        return vars(self)
