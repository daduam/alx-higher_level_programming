#!/usr/bin/python3
"""Print Square"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size of the square.

    Raises:
        TypeError: If `size` is not of type int.
        ValueError: If `size` is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
