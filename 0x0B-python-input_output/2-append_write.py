#!/usr/bin/python3
"""Defines file-appending funct."""


def append_write(filename="", text=""):
    """Appends string to the end of UTF8 text file.

    Args:
        filename (str): The name of file to append to.
        text (str): The string append to the file.
    Returns:
        The numb of char appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
