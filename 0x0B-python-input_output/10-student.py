#!/usr/bin/python3
'''class Student that defines a student '''


class Student:
    '''class that defines a student'''
    def __init__(self, first_name, last_name, age):
        '''initialisation of attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''method that retrieves a dictionary representation of a\
 Student instance'''
        if not attrs:
            return self.__dict__
        return ({key: getattr(self, key) for key in attrs if
                 hasattr(self, key)})
