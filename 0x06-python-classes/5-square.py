#!/usr/bin/python3

"""Defines a Square class to represent a square."""


class Square:
    """Represent a square.

    Attributes:
        size (int): The size of one side of the square.
                    Default 0 if no argument passed.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of one side of the square.
                        Default 0 if no argument passed.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    def area(self):
        """Calculate and return the area of the square instance.

        Returns:
            int: The calculated area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square side.

        Returns:
            int: The current size of the square side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square side.

        Args:
            value (int): The size of the square side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print the square with '#'.
        """
        if self.__size == 0:
            print()
        else:
            print((("#" * self.__size + "\n") * self.__size), end="")
