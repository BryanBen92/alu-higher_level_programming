#!/usr/bin/python3
"""Read a Python object from a JSON file."""


import json


def load_from_json_file(filename):
    """Return the Python object stored in the given JSON file."""
    with open(filename, encoding="utf-8") as stream:
        return json.load(stream)
