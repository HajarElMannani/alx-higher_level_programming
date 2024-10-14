#!/usr/bin/python3
'''Define class Square that inherits from Rectangle'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''a class that enhirits from the class Rectangle'''

    def __init__(self, size):
        '''instantiantion of the class Square
        args:
           size(int): size of the square
        Return: Nothing
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''area of a square
        Return:
            areqof the square'''
        return (self.__size ** 2)
