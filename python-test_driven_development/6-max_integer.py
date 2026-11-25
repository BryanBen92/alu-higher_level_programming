#!/usr/bin/python3
"""Find the maximum element in a list."""


def max_integer(list=[]):
    """Return the largest item or None for an empty list."""
    if len(list) == 0:
        return None
    result = list[0]
    index = 1
    while index < len(list):
        if list[index] > result:
            result = list[index]
        index += 1
    return result
