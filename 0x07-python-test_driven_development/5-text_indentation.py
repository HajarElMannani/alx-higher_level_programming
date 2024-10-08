#!/usr/bin/python3
'''function text_indetation'''


def text_indentation(text):
    '''function that parses a text when ".:?"are found
    args:
       text (str):text to parse
    '''
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        i = 0
        if text == "":
            print("", end="")
        elif text[0] == " ":
            while text[i] == " ":
                i += 1
        while i < len(text):
            if text[i - 1] == "." and text[i] == " ":
                i += 1
                print("\n")
            elif text[i - 1] == ":" and text[i] == " ":
                i += 1
                print("\n")
            elif text[i - 1] == "?" and text[i] == " ":
                i += 1
                print("\n")
            else:
                print("{}".format(text[i]), end="")
                i += 1
