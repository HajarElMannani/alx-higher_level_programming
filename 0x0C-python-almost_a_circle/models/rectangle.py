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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''return string to print
        Return: a string'''
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
                f"- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        '''public method that assigns an argument to each attribute
        args:
            *args(int): arguments to assign to attributes
            **kwargs(key/value): double pointerto dictionary
        Return: nothing'''
        attributes = ['id', 'width', 'height', 'x', 'y']
        if (args):
            for i, arg in enumerate(args):
                if i < 5:
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''method returns the dictionary representation of a Rectangle
        Return: dictionary representation'''
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}
