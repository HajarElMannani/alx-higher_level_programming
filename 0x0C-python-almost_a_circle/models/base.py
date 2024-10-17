#!/usr/bin/python3
'''the class Base'''


class Base():
    '''the class Base is the base class for this project'''
    __nb_objects = 0
    
    def __init__(self, id=None):
        '''initialisation of the class
        args:
            id(int): id of the class
        Return: Nothing'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
