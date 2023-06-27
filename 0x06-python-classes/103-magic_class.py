#!/usr/bin/python3
"""
This module defines the MagicClass that performs various calculations based on radius.
"""

import math


class MagicClass:
    """
    Represents a MagicClass that performs calculations based on radius.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (int or float): The radius of the circle. Default is 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
