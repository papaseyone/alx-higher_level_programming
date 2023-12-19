#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of a square (based on 1-square.py).

    Attributes:
        size (int): Size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of a square.

        Args:
            size (int): Size of the square (1 side).

        Raises:
            TypeError: Size must be an integer.
            ValueError: Size must be >= 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
