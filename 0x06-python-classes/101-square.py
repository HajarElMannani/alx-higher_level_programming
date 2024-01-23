#!/usr/bin/python3
"""class Square that defines a square by size"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @property
    def position(self):
        """retrieve the position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """set tuple
        args:
            value (int):positon value
        """
        if type(value[0]) and type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return Area of a square"""
        return (self.__size*self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        if self.__position[1] > 0:
            for k in range(0, self.__position[1]):
                print("")
        for i in range(0, self.__size):
            if self.__position[0] > 0:
                for b in range(0, self.__position[0]):
                    print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
