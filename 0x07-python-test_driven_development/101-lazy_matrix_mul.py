#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using the NumPy module.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        The resulting matrix.

    Raises:
        ValueError: If the matrices cannot be multiplied.
"""

    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)
    
    result = matrix_a @ matrix_b

    return result

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
