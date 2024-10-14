#!/usr/bin/python3
'''contains a function lookup'''


def lookup(obj):
    ''' function that returns the list of available \
attributes and methods of an object
Return a list
'''
    return dir(obj)
