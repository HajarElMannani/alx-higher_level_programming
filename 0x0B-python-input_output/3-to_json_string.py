#!/usr/bin/python3
''' function to_json_string returns the JSON representation of an object '''
import json


def to_json_string(my_obj):
    '''function that returns the JSON representation of an object (
    args:
        my_obj(any): object to give string represention of
    Return: the JSON representation of an object '''
    return json.dumps(my_obj)
