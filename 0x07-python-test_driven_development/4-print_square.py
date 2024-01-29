#!/usr/bin/python3
'''function print_square'''


def print_square(size):
    '''print square of a given size
    args:
        size (int): size of the square
    '''
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
