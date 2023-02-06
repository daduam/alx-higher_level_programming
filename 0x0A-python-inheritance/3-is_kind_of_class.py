#!/usr/bin/python3
"""Is Kind of Class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj (Any): The object.
        a_class (Class): The class.

    Returns:
        True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class.
        Otherwise False.
    """
    return isinstance(obj, a_class)
