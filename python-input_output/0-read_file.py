#!/usr/bin/python3
"""Read a UTF-8 text file."""


def read_file(filename=""):
    """Print the entire file without adding a newline."""
    with open(filename, encoding="utf-8") as stream:
        print(stream.read(), end="")
