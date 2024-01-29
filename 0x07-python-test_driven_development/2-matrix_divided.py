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
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    row_len = []
    i = 0
    for row in matrix:
        for row[i] in row:
            if type(row[i]) is not int and type(row[i]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_len.append(len(row))
    for j in row_len:
        if j != row_len[0]:
            raise TypeError("Each row of the matrix must have the same size")
    divl = []
    k = 0
    divl = [[round(elem / div, 2) for elem in row] for row in matrix]
    return divl
