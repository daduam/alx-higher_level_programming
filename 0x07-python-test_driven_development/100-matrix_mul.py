#!/usr/bin/python3
"""Matrix Multiplication"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (list): Matrix A
        m_b (list): Matrix B

    Returns:
        The matrix result of A x B

    Raises:
        TypeError: If `m_a` or `m_b` is not a list of lists of ints
            or floats. If each row of `m_a` are not of the
            same size, also for `m_b`.
        ValueError: If `m_a` or `m_b` is empty, or if `m_a` and `m_b`
            cannot be multiplied.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")

    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if any(type(row) != list for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if any(type(row) != list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if any(
        type(elem) not in (int, float)
        for elem in [x for row in m_a for x in row]
    ):
        raise TypeError("m_a should contain only integers or floats")

    if any(
        type(elem) not in (int, float)
        for elem in [x for row in m_b for x in row]
    ):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a*b for a, b in zip(a_row, b_col))
            for b_col in zip(*m_b)] for a_row in m_a]
