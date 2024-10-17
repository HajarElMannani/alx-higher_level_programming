#!/usr/bin/python3
'''Class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''a class that inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialisation of the class Rectangle
        args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): coordinate x
            y(int): coordinate y
            id(int): id of the class
        Return: nothing'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter for width
        Return: width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width
        args:
            value(int): value of width'''
        #width and height must be int and positive
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        '''getter for height
        Return: height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height
        args:
        value(int): value of height'''
        # value must be int and positive
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter for x
        Return: x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x
        args:
            value(int): value of x'''
        #conditions on x
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter for y
        Return: y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y
        args:
        value(int): value of y'''
        #conditions on y
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        '''area of the triangle
        Return: area'''
        return (self.__width * self.__height)

    def display(self):
        '''that prints in stdout the Rectangle instance with the
 character #
        Return: Nothing'''
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
