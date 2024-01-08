#!/usr/bin/python3
"""Defines class and inherited class-checking funct."""


def is_kind_of_class(obj, a_class):
    """Check if an obj is an instance or inherited instance of a class.

    Args:
        obj (any): The obj to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
