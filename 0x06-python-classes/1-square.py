#!/usr/bin/python3
"""class Square that defines a square by size"""


class Square:
    """defines a square by size"""
    def __init__(self, size):
        """Instantiation with size
        args:
            size (int): size of the square
        Returns:
            nothing
        """
        self.__size = size
