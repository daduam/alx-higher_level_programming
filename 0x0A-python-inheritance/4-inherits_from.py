#!/usr/bin/python3
"""Inherits From"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (Any): The object.
        a_class (Class): The class.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class.
        Otherwise False.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
