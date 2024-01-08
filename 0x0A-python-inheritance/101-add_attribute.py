#!/usr/bin/python3
"""Defines function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new att. to an obj. if possible.

    Args:
        obj (any): The object to add an att. to.
        att (str): The name of the att. to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
