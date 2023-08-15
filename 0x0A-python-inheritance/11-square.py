#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the square in the \
format [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
