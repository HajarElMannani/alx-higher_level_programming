#!/usr/bin/python3
'''the function is_same_class checks instance of class'''


def is_same_class(obj, a_class):
    '''function that returns True if the object is exactly\
    an instance of the specified class ; otherwise False
    args:
        obj(any): object to check out
        a_class(type): class to verify if the object is an instance of
    Return:
        True if it belongs, False if not
    '''

    if type(obj) is a_class:
        return True
    else:
        return False
