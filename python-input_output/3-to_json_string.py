#!/usr/bin/python3
"""Serialize a Python object as JSON."""


import json


def to_json_string(my_obj):
    """Return the JSON string for a Python object."""
    return json.dumps(my_obj)
