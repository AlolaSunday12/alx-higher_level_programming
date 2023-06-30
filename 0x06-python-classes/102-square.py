#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    def __lt__(self, other):
        """
        Less than comparator.

        Args:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the area of self is less than the area of other, False otherwise.
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        Less than or equal to comparator.

        Args:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the area of self is less than or equal to the area of other, False otherwise.
        """
        return (self.area() <= other.area())

    def __eq__(self, other):
        """
        Equality comparator.

        Args:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the area of self is equal to the area of other, False otherwise.
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        Not equal to comparator.

        Args:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the area of self is not equal to the area of other, False otherwise.
        """
        return (self.area() != other.area())

    def __gt__(self, other):
        """
        Greater than comparator.

        Args:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the area of self is greater than the area of other, False otherwise.
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        Greater than or equal to comparator.

        Args:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the area of self is greater than or equal to the area of other, False otherwise.
        """
        return (self.area() >= other.area())
