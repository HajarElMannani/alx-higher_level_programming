#!/usr/bin/python3
'''function that divides a matrix by a given number'''


def matrix_divided(matrix, div):
    '''divide matrix by the number div
    args:
        matrix: a matrix
        div (int): integer to divide matrix by
    Returns:
        divided matrix
    '''
    div_matrix = [[]]
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(div) != int) and (type(div) != float):
        raise TypeError("div must be a number")
    for row in matrix:
        for i in row:
            if (type(i) != int) and (type(i) != float):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    div_matrix = [[round((num / div), 2) for num in row] for row in matrix]
    return (div_matrix)
