#!/usr/bin/python3
"""
    This module contains a function to print pascal triangle
"""


def pascal_triangle(n):
    """ Function that returns a list of lists of integers representing the
    Pascal’s triangle of n

    Args:
        n: lines of inner lists

    Returns:
        a list of lists
    """
    outer_list = []
    if n <= 0:
        return outer_list
    outer_list =[[1]]

    for i in range(1, n):
        inner_list = [1]
        for j in range(1, i):
            inner_list.append(outer_list[i - 1][j - 1] + outer_list[i - 1][j])
        inner_list.append(1)
        outer_list.append(inner_list)
    return outer_list
