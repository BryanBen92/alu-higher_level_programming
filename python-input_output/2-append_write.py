#!/usr/bin/python3
"""Append to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append to the file and return the number of characters written."""
    with open(filename, "a", encoding="utf-8") as stream:
        return stream.write(text)
