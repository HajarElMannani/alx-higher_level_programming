#!/usr/bin/python3
''' the function inerits_from chechs if object is instance\
of a class that inerited of a class'''


def inherits_from(obj, a_class):
    '''
    if the object is an instance of a class that inherited\
     (directly or indirectly) from the specified class
    args:
        obj(any): object to check out
        a_class(type): class to check out if obj is instance\
     of class inherited of
    Return:
        True if it belongs, False otherwise
    '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
