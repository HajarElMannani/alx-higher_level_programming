#!/usr/bin/python3
"""class Square that defines a square by size"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value of the size
        args:
            value (int):size of square
        """
        if type(value) is int:
            self.__size = value
            if value < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """return Area of a square"""
        return (self.__size*self.__size)
