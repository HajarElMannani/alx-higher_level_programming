#!/usr/bin/python3
'''class Rectangle that defines a rectangle'''


class Rectangle:
    '''class Rectangle'''
    def __init__(self, width=0, height=0):
        '''inatantiation of class Rectangle'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
