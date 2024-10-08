#!/usr/bin/python3
'''class Rectangle that defines a rectangle'''


class Rectangle:
    '''class Rectangle'''
    def __init__(self, width=0, height=0):
        '''inatantiation of class Rectangle
        args:
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width getter
        Returns:
            width value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter
        args:
            value (int): value of width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height getter
        Returns:
            height value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter
        args:
            value (int): value of height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        '''area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        '''print rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        figure = (row + '\n') * self.__height
        figure = figure.strip()
        return figure

    def __repr__(self):
        '''return string representation'''
        return "Rectangle ({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''delete instance'''
        print("Bye rectangle...")
