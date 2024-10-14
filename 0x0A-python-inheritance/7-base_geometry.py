#!/usr/bin/python3
'''empty class BaseGeometry'''


class BaseGeometry():
    '''empty class'''

    def area(self):
        '''raise an exception
         Return: nothing
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' function that that validates value
        args:
            name(str): a name
            value(int): a value
        Return: Nothing
        raise:
            TypeError if vaue is not int
            Value Error if value is < 0
        '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
