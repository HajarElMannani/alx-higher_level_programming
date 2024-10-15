#!/usr/bin/python3
'''function write_file that writes a string to text file'''


def write_file(filename="", text=""):
    '''function that writes a string to a text file 
    args:
        filename(FILE): pat of the text file
        text(str): string to add to file
    Return:
        number of character written'''
    with open(filename, 'w', encoding="UTF-8") as my_file:
        return my_file.write(text)
