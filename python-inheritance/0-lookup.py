#!/usr/bin/python3
"""Inspect an object's available attributes."""


def lookup(obj):
    """Return the names available on the object."""
    return dir(obj)
