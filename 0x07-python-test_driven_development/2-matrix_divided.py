#!/usr/bin/python3
"""My Function module"""


def matrix_divided(matrix, div):
    """A function that divides all the element of a matrix"""

    error = "matrix must be a matrix (list of lists) of integers/floats"
    error_same_size = "Each row of the matrix must have the same size"
    if matrix is None or len(matrix) == 0:
        raise TypeError(error)
    for lst in matrix:
        if lst is None or not isinstance(lst, list) or len(lst) == 0:
            raise TypeError(error)
    new_mtrx = matrix[:]
    for i in range(len(matrix)):
        while (i != (len(matrix) - 1)):
            if len(matrix[i]) != len(matrix[i+1]):
                raise TypeError(error_same_size)
            i += 1
    for lst in (matrix):
        for i in range(len(lst)):
            if type(lst[i]) not in [int, float]:
                raise TypeError(error)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    index = 0
    for lst in matrix:
        new_mtrx[index] = (list(map(lambda x: round(x / div, 2), lst)))
        index += 1
    return new_mtrx
