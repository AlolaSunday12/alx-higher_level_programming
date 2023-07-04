#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""

def say_my_name(first_name, last_name=""):
    """
    Prints the name based on the provided first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        full_name = "My name is {} {}".format(first_name, last_name)
    else:
        full_name = "My name is {}".format(first_name)

    print(full_name)
