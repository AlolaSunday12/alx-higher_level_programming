#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a: The first matrix as a 2D array-like object.
        m_b: The second matrix as a 2D array-like object.

    Returns:
        The resulting matrix as a NumPy array.

    Raises:
        ValueError: If the matrices cannot be multiplied due to incompatible dimensions.
    """

    return np.matmul(m_a, m_b)
