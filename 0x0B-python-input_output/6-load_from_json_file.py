#!/usr/bin/python3
'''function load_from_json_file that creates an Object from a “JSON file”'''
import json


def load_from_json_file(filename):
    '''function that creates an Object from a “JSON file”
    args:
        filename(FILE): the json file
    Return: object created'''
    with open(filename, 'r', encoding="UTF-8") as my_file:
        for obj in my_file:
            return json.loads(obj)
