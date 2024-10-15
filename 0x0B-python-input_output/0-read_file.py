#!/usr/bin/python3
'''function read_file print to stdout'''


def read_file(filename=""):
    '''function that reads a text file (UTF8) and prints it to stdout
    args:
        filename(FILE): pah of the file to read
    Return: Nothing'''

    with open(filename, 'r', encoding="UTF-8") as my_file:
        print(my_file.read(),end='')
