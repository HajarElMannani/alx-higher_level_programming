#!/usr/bin/python3
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class TestBase(unittest.TestCase):

    def test_valid_init(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_valid_init1(self):
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_valid_init2(self):
        base = Base(None)
        self.assertEqual(base.id, 2)

    def test_change_id(self):
        base = Base(5)
        base.id = 9
        self.assertEqual(base.id, 9)

    def test_two_args_base(self):
        with self.assertRaises(TypeError):
            Base(2, 3)


class TestToJsonString(unittest.TestCase):

    def Test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        json_dictionary = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(str(json_dictionary), [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}])

    def test_to_json_string_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 7, 8, 5, 3)
        json_dictionaries = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(len(json_dictionaries), 105)

    def test_to_json_string_square(self):
        s1 = Square(10, 7, 8, 1)
        json_dictionary = Base.to_json_string([s1.to_dictionary()])
        self.assertEqual(len(json_dictionary), 39)

    def test_to_json_string_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_list_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 2)

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestSaveToFile(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as my_file:
            output = my_file.read()
        self.assertEqual(json.loads(output), [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}
        ])

    def test_seve_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as my_file:
            output = my_file.read()
        self.assertEqual(json.loads(output), [])

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as my_file:
            output = my_file.read()
        self.assertEqual(output, "[]")

    def test_save_to_file_two_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], [2])

    def test_save_to_file_no_argmnt(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestFromJsonString(unittest.TestCase):

    def test_from_json_string(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}])

    def test_from_json_string_two(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_square(self):
        list_input = [{"id": 89, "size": 10}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_empty(self):
        output = Base.from_json_string("[]")
        self.assertEqual(output, [])

    def test_from_json_string_None(self):
        output = Base.from_json_string(None)
        self.assertEqual(output, [])

    def test_from_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([1, 2], [2])

    def test_from_json_string_no_argmnt(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestCreate(unittest.TestCase):

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_create_is_equal(self):
        r1 = Rectangle(3, 5, 2, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 == r2)

    def test_create_rectangle_1(self):
        r1 = Rectangle(4, 5, 9, 2, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (4) 9/2 - 4/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(4, 5, 9, 2, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (4) 9/2 - 4/5", str(r2))

    def test_create_is(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)

    def test_create_square(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))

    def test_create_is_equal_square(self):
        s1 = Square(3, 5, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 == s2)

    def test_create_is_square(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)

    def test_create_square_original(self):
        s1 = Square(6, 9, 3, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (1) 9/3 - 6", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 8, 1, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (2) 8/1 - 3", str(s2))



class TestLoadFromFiles(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_2_rectangle(self):
        r1 = Rectangle(1, 7, 8, 5, 7)
        r2 = Rectangle(2, 9, 3, 4, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_two_rectangle(self):
        r1 = Rectangle(2, 4, 5, 3, 1)
        r2 = Rectangle(5, 8, 5, 9, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_type(self):
        r1 = Rectangle(2, 4, 5, 3, 1)
        r2 = Rectangle(5, 8, 5, 9, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangle_output = Rectangle.load_from_file()
        self.assertTrue((type(obj) is Rectangle for obj in list_rectangle_output))

    def test_load_from_file_square(self):
        s1 = Square(10, 7, 2, 1)
        list_squares_input = [s1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_2_square(self):
        s1 = Square(2, 1, 8, 6)
        s2 = Square(7, 1, 3, 8)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_two_square(self):
        s1 = Square(2, 4, 5, 1)
        s2 = Square(5, 8, 5, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_type_square(self):
        s1 = Square(2, 4, 5, 1)
        s2 = Square(5, 8, 5, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertTrue((type(obj) is Square for obj in list_squares_output))

    def test_load_from_file_two_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([1], [1, 2])

    def test_load_from_file_no_file(self):
        square = Square.load_from_file()
        self.assertEqual([], square)


if __name__ == '__main__':
    unittest.main()
