#!/usr/bin/python3
"""Is Same Class"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj (Any): The object.
        a_class (Class): The class

    Returns:
        True if the object is exactly an instance of the specified class.
        Otherwise False.
    """
    return type(obj) == a_class
