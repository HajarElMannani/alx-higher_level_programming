#!/usr/bin/python3
'''class Rectangle that defines a rectangle'''


class Rectangle:
    '''class Rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''inatantiation of class Rectangle
        args:
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        for i in range(self.__height - 1):
            print(str(self.print_symbol) * self.__width)
        return (str(self.print_symbol) * self.__width)

    def __repr__(self):
        '''return string representation'''
        return "Rectangle ({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''delete an instance'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return rectangle with the greatest area'''
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("ect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        '''returns a square'''
        new_rec = Rectangle(size, size)
        return new_rec
