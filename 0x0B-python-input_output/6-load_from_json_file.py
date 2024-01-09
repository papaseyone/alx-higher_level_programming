#!/usr/bin/python3
"""Defines JSON file-reading funct."""
import json


def load_from_json_file(filename):
    """Create Python obj from JSON file."""
    with open(filename) as f:
        return json.load(f)
