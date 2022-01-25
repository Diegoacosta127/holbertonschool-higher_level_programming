#!/usr/bin/python3
"""module 2-matrix_divided"""


def matrix_divided(matrix, div):
    """divides all values in a matrix by a given value"""
    new_list = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats")
            else:
                new_row.append(round((elem / div), 2))
        new_list.append(new_row)
    return new_list
