#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''rest thefunction max_integer'''

    def test_empty_list(self):
        '''test when list is empty'''
        self.assertEqual(max_integer(list=[]), None)
        self.assertEqual(max_integer(list=[None]), None)

    def test_positive_list(self):
        '''test when list is of positive numbers'''
        self.assertEqual(max_integer(list=[5, 3, 6, 2, 1]), 6)

    def test_negative_list(self):
        '''test a list of negative numbers'''
        self.assertEqual(max_integer(list=[-5, -6, -4, -2]), -2)

    def test_mixed_num(self):
        '''test a list of positive and negative numbers'''
        self.assertEqual(max_integer(list=[-2, 3, 9, -5, 0]), 9)

    def test_list_of_zeros(self):
        '''test a list of zeros only'''
        self.assertEqual(max_integer(list=[0, 0, 0, 0]), 0)

    def test_list_of_one(self):
        '''test a list containing only one integer'''
        self.assertEqual(max_integer(list=[9]), 9)


if __name__ == '__main__':
    unittest.main()
