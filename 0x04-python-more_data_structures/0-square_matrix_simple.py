#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        m = []
        new.append(m)
        for j in i:
            m.append(j ** 2)
    return new
