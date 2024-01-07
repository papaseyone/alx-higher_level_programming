#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix contains non-numbers or not properly formatted.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If divisor is not an int or float.
        ZeroDivisionError: If the divisor is 0.

    Returns:
        list: A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for row in matrix for ele in row)):
        raise TypeError("matrix a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
