#!/usr/bin/python3
''' function pascal_triangle '''


def pascal_triangle(n):
    '''function that returns a list of lists of integers\
representing the Pascal’s triangle of n
    args:
       n(int): an integer
    Return: list of lists of integers'''
    pascal = []
    if n <= 0:
        return []
    first = [1]
    for i in range(n):
        line = first * (i + 1)
        for j in range(1, i):
            line[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(line)
    return pascal
