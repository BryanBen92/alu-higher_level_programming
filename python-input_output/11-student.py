#!/usr/bin/python3
"""Serialize and restore student information."""


class Student:
    """Store identifying information for a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return attributes selected by a list of names, or all attributes."""
        attributes = vars(self)
        is_list = isinstance(attrs, list)
        if is_list and all(isinstance(name, str) for name in attrs):
            return {name: attributes[name] for name in attrs
                    if name in attributes}
        return attributes

    def reload_from_json(self, json):
        """Update the student's attributes from a dictionary."""
        vars(self).update(json)
