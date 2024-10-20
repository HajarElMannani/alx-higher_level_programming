#!/usr/bin/python3
'''Class Square that inherits from Rectangle'''
from models.rectangle import Rectangle

class Square(Rectangle):
    '''A class that inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialisation of the class Square'''
        super().__init__(size, size, x, y, id)
 

    @property
    def size(self):
        '''getter for size
        Return: size'''
        return self.width

    @size.setter
    def size(self, value):
        '''set value for size
        args:
            value(int): value of size
        Return: Nothing'''
        try:
            self.width = value
            self.height = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        
    def __str__(self):
        '''return string to print
        Return: string'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        '''function that assigns attributes
        args:
            args(int): no-keyworded arguments
            kwargs(key/value): keyworded arguments
        Return: Nothing'''
        attributes = ['id', 'size', 'x', 'y']
        if (args):
            for i, arg in enumerate(args):
                if i < 4:
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary representation of a Square
        Return: a dictionary reprentation'''
        return {"id": self.id, "size": self.__size, "x": self.x, "y": self.y}
