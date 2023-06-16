#!/usr/bin/python3

"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix and returns a new matrix.

    Args:
    matrix: The list of lists.
    div: The divisor.

    Returns:
    A new matrix.

    Raises:
    TypeError: If the elements in matrix aren't integer or float numbers
    TypeError: If each row of the matrix doesn't have the same size
    TypeError: divisor is not a number
    ZeroDivisionError: division by zero
    """

    type_message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(type_message)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(type_message)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(type_message)

    size_message = "Each row of the matrix must have the same size"
    row_size = 0
    for i in range(len(matrix)):
        if i == 0:
            row_size = len(matrix[i])
        if len(matrix[i]) != row_size:
            raise TypeError(size_message)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf'):
        return list(map(lambda row: list(map(lambda num: 0.0, row)), matrix))

    return list(map(
        lambda row: list(map(
            lambda num: round(num / div, 2), row)), matrix))
