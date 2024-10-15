#!/usr/bin/python3
'''Function append_write that appends a stringat the end of text file'''


def append_write(filename="", text=""):
    '''function that appends a string at the end of a text file
    args:
        filename(FILE): path to the file
        text(str): string to append
    Return:  the number of characters added'''
    with open(filename, 'a', encoding="UTF-8") as my_file:
        return my_file.write(text)
