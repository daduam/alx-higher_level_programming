#!/usr/bin/python3
"""Lookup"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (Any): Object of interest.

    Returns:
        List of available attributes and methods of `obj`.
    """
    return dir(obj)
