#!/usr/bin/python3
"""Represents a square and its properties."""


class Square:
    """
    Models a square with a single side length.

    Attributes:
        side_length: (private) The length of one side of the square.
    """

    def __init__(self, side_length):
        """
        Initializes a new Square object.

        Args:
            side_length: The length of one side of the square.
        """
        self.__side_length = side_length
