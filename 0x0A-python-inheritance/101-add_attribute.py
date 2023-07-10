#!/usr/bin/python3
"""
Defines a function that adds a new attribute to an object if possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Raises a TypeError if the object can't have a new attribute.

    Args:
        obj: The object to add the attribute to.
        attr: The attribute name.
        value: The attribute value.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
