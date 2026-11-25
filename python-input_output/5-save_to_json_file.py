#!/usr/bin/python3
"""Save a Python object to a JSON file."""


import json


def save_to_json_file(my_obj, filename):
    """Write the object's JSON representation to the given file."""
    with open(filename, "w", encoding="utf-8") as stream:
        json.dump(my_obj, stream)
