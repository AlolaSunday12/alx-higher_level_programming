#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list[list]): The matrix, a list of lists.
        div (int or float): The divisor.

    Returns:
        list[list]: The resulting matrix with the divided elements.

    Raises:
        TypeError: If the matrix is not a list of lists or contains \
 non-numeric values.
        TypeError: If the matrix rows have different sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list)
 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
 integers/floats")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("matrix must have each row with the same size")

        if any(not isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of \
 integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
