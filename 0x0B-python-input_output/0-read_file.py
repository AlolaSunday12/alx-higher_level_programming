#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Print the contents of a UTF8 text file to stdout.

    Args:
        filename (str, optional): The name of the file to \
read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
