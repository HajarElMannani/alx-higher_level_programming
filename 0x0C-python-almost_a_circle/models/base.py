#!/usr/bin/python3
'''the class Base'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''method that returns the JSON string representation of/
 list_dictionaries
        args:
            list_dictionaries(list): list of dictionaries
        Return: JSON string representation'''
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    

    @classmethod
    def save_to_file(cls, list_objs):
        '''method that writes the JSON string representation of/
 list_objs to a file
        args:
            list_objs(list): list of instances who inherits of Base
        Return: Nothing'''
        filename  = f"{cls.__name__}.json"
        with open(filename, 'w') as my_file:
            if (list_objs is None) or (not list_objs):
                my_file.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                my_file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation\
 json_string
        args:
            json_string(str): string representing list of\
 dictionnaries        
        Return: a list of json string reprentation'''
        if not json_string:
            return [] 
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        '''method that returns an instance with all attributes/
 already set
        args:
            dictionary(dict): a dictionary
        Return:  instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1, 1, 1)
        dummy.update(**dictionary)
        return dummy

        
    @classmethod
    def load_from_file(cls):
        '''method that returns a list of instances
        Return: list of instances'''
        filename = f"{cls.__name__}.json"
        if not filename:
            return []
        with open(filename, 'r') as my_file:
            list_dictionaries = cls.from_json_string(my_file.read())
            instances = [cls.create(**dictionary) for dictionary in list_dictionaries]
            return instances
