#!/usr/bin/python3
"""Deserialize a JSON string."""


import json


def from_json_string(my_str):
    """Return the Python value encoded in a JSON string."""
    return json.loads(my_str)
