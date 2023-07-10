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

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 1.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
