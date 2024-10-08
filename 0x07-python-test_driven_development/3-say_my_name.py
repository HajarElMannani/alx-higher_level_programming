#!/usr/bin/python3
'''function that prints first name and last name'''


def say_my_name(first_name, last_name=""):
    '''print first name and last  name
    args:
        first_name (str): first name to print
        last_name (str): family name to print
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
