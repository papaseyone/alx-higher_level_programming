#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Prevent the addition of new attributes except for 'first_name'.

    Attributes:
        __slots__ (list): A list containing only 'first_name' as an allowed attribute.
    """

    __slots__ = ["first_name"]

