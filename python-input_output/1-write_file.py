#!/usr/bin/python3
"""Overwrite a UTF-8 text file."""


def write_file(filename="", text=""):
    """Overwrite the file and return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as stream:
        return stream.write(text)
