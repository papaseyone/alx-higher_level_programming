#!/usr/bin/python3
"""Defines Python class-to-JSON funct."""


def class_to_json(obj):
    """Return dict. represntation of simple data struct."""
    return obj.__dict__
