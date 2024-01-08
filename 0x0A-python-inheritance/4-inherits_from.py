#!/usr/bin/python3
"""Defines inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an obj is an inherited instance of a class.

    Args:
        obj (any): The obj to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
