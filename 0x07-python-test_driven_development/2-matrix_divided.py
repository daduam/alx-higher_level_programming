#!/usr/bin/python3
"""Matrix Divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): List of lists of ints or floats.
        div (int|float): Integer to divide through matrix with.

    Returns:
        A new matrix with elements of the original matrix divided by div.

    Raises:
        TypeError: If `matrix` is not a list of lists of numbers, if the
            length of all the rows of `matrix` are not the same, or if `div`
            is not a number
        ZeroDivisionError: If `div` is 0.
    """
    if (
        not matrix
        or type(matrix) != list
        or any(type(row) != list for row in matrix)
        or any(
            type(elem) not in (int, float)
            for elem in [x for row in matrix for x in row]
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x/div, 2), row)) for row in matrix]
