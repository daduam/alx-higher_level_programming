#!/usr/bin/python3
"""Say My Name"""


def say_my_name(first_name, last_name=""):
    """Prints the names passed.

    Args:
        first_name (str): First name.
        last_name (:obj:`str`, optional): Last name. Defaults to empty string.

    Raises:
        TypeError: if `first_name` or `last_name` is not of type `str`.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
