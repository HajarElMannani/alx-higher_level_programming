#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in range(len(matrix)):
            for i in range(len(matrix[line])):
                if i != len(matrix[line]) - 1:
                    ends = " "
                else:
                    ends = ""
                print("{:d}".format(matrix[line][i]), end=ends)
            print()
