#!/usr/bin/python3
''' function is_kind_of_classchecks if an obect is instance of a class'''


def is_kind_of_class(obj, a_class):
    '''if the object is an instance of, or if the object is\
     an instance of a class that inherited from, the specified class
    args:
        obj(any): object to check out
        a_class(type):class to ferify if obj is an instance of
    Return:
        True if obj is inctance of class, False otherwise
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
