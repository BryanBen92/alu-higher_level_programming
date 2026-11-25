#!/usr/bin/python3
"""Check for a strict subclass instance."""


def inherits_from(obj, a_class):
    """Check for a strict subclass instance."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
