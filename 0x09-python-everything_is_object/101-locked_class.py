#!/usr/bin/python3
"""Define a locked class."""

class LockedClass:
    """
    A class that restricts the user from dynamically creating
    new instance attributes,
    except for the 'first_name' attribute.

    Attributes:
        __slots__ (list[str]): List of allowed attribute names.
    """

    __slots__ = ["first_name"]
