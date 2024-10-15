#!/usr/bin/python3
'''function that returns the dictionary description with simple data\
 structure'''


def class_to_json(obj):
    '''function that returns the dictionary description with simple\
 data structure (list, dictionary, string, integer and boolean) for JSON\
 serialization of an object
    args:
        obj(any): is an instance of a Class
    return: the dictionary description '''
    return obj.__dict__
