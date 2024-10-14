#!/usr/bin/python3
'''function Rectangle that enhitits from BaseGeometry'''

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

    def area(self):
        '''area of a rectangle
        args:
            nothing
        Return: area of the rectangle'''
        return (self.__width * self.__height)

    def __str__(self):
        '''Return: expression to be printed'''
        return f"[Rectangle] {self.__width}/{self.__height}"
