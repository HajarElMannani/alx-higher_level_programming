#!/usr/bin/python3
'''class that inherits from list'''


class MyList(list):
    '''a class that enherits from the class list'''

    def print_sorted(self):
        '''print a sorted list
        args:
            self(any): object
        Return:
            Nothing
        '''
        print(sorted(self))
