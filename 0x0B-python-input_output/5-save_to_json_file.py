#!/usr/bin/python3
'''function save_to_json_file that writes an Object to a text file,'''
import json


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file,\
using a JSON representation
    args:
        my_obj(any): object to write as string
        filename(FILE): path to text file
    Return: Nothing'''
    with open(filename, 'w', encoding="UTF-8") as my_file:
        my_file.write(json.dumps(my_obj))
