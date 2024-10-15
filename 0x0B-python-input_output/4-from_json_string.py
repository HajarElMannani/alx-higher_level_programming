#!/usr/bin/python3
''' function from_json_string that returns an object (Python data\
structure) represented by a JSON string'''
import json


def from_json_string(my_str):
    '''function that returns an object (Python data structure)\
represented by a JSON string
    args:
       my_str(str): string to return as object
    Return: an object (Python data structure) represented by a JSON string'''
    return json.loads(my_str)
