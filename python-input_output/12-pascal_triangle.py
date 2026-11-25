#!/usr/bin/python3
"""Build Pascal's triangle."""


def pascal_triangle(n):
    """Return the first n rows of Pascal's triangle as lists."""
    rows = []
    for _ in range(n):
        if not rows:
            rows.append([1])
            continue
        previous = rows[-1]
        middle = [left + right for left, right in zip(previous, previous[1:])]
        rows.append([1] + middle + [1])
    return rows
