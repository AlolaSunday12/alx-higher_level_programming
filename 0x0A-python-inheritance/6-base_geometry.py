#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry(object):
    """Represent base geometry."""

    def area(self):
        """Compute the area.

        Raises:
            Exception: Indicates that the area() method is not implemented.

        """
        raise Exception("area() is not implemented")
