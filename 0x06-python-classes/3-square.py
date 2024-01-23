#!/usr/bin/python3
"""class Square that defines a square by size"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        """Instantiation with size
        args:
            size (int): size of the square
        Returns:
            nothing
        """
        if type(size) is int:
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """return Area of a square"""
        return (self.__size*self.__size)
