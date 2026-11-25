#!/usr/bin/python3
"""Expose instance attributes for JSON serialization."""


def class_to_json(obj):
    """Return a dictionary describing the object's instance attributes."""
    return vars(obj)
