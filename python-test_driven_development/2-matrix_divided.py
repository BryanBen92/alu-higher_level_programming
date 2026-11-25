#!/usr/bin/python3
"""Divide a rectangular matrix without modifying the original."""


def matrix_divided(matrix, div):
    """Return a matrix of quotients rounded to two decimal places."""
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(matrix_error)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_error)
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(matrix_error)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
