#!/usr/bin/python3
"""Defines a class representing a square."""


class Square:
    """
    Models a square with a single side length.

    Attributes:
        _size (private): The length of one side of the square
            (must be an integer >= 0).

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object with a validated side length.

        Args:
            size (int, optional): The length of one side of the
                square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
