#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError:  If either of a or b is a non-integer and non-float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
