#!/usr/bin/python3
"""Defines object attribute lookup funct."""


def lookup(obj):
    """Return list of object's available attributes."""
    return (dir(obj))
