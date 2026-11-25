#!/usr/bin/python3
"""Print a name composed of a first name and an optional last name."""


def say_my_name(first_name, last_name=""):
    """Print the name after validating both components."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
