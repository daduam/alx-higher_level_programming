#!/usr/bin/python3
"""Lazy Matrix Multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.

    Args:
        m_a (list): Matrix A
        m_b (list): Matrix B

    Returns:
        A x B
    """
    return np.matmul(m_a, m_b)
