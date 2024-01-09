#!/usr/bin/python3
"""Defines file-writing funct."""


def write_file(filename="", text=""):
    """Write string to UTF8 text file.

    Args:
        filename (str): The name of file to write.
        text (str): The text write to the file.
    Returns:
        The numb of char written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
