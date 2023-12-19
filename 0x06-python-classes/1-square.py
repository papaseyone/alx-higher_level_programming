#!/usr/bin/python3

"""Defines a Square class representing a square."""


class Square:
    """Represent a square.

    Attributes:
        size (int): The size of the square (length of one side).
    """

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square
                (length of one side).
        """
        self.__size = size
