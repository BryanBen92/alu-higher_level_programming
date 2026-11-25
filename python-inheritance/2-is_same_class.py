#!/usr/bin/python3
"""Check for an exact class match."""


def is_same_class(obj, a_class):
    """Check for an exact class match."""
    return type(obj) is a_class
