#!/usr/bin/python3
'''the function Rectangle is a subclass of BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class that inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''instantiation of Rectangle
        args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        Return: nothing
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
