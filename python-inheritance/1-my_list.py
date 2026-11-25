#!/usr/bin/python3
"""Provide a list with a sorted printing method."""


class MyList(list):
    """Extend a list with a sorted display."""

    def print_sorted(self):
        """Print the items in order without mutating the list."""
        print(sorted(self))
