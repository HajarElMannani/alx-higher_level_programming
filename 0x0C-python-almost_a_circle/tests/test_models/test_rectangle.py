import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(1, 1, 0, 0, None)

    def test_valid_init(self):
        rectangle = Rectangle(10, 2)
        self.assertEqual(rectangle.id, 2)

    def test_valid_init1(self):
        rectangle = Rectangle(2, 10)
        self.assertEqual(rectangle.id, 3)

    def	test_valid_init1(self):
        rectangle = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rectangle.id, 12)


class TestHeight(unittest.TestCase):
    '''test values of height'''
    def test_negative_heiht(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, -2)
        self.assertEqual(str(context.exception), "height must be > 0")


    def test_string_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(5, "be")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_None_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(3, None)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_list_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(4, [1, 2])
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_tuple_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, (1,))
        self.assertEqual(str(context.exception), "height must be an integer")
        
    def test_float_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 0.2)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_dict_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, {"height": 1})
        self.assertEqual(str(context.exception), "height must be an integer")
    


class TestWidth(unittest.TestCase):     
    '''test values of width'''

    def test_negative_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(-10, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_string_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("a string", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_None_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(None, 2)
        self.assertEqual(str(context.exception), "width must be an integer")
        
    def test_list_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle([1, 2], 2)
        self.assertEqual(str(context.exception), "width must be an integer")
        
    def test_tuple_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle((1,), 2)
        self.assertEqual(str(context.exception), "width must be an integer")
        
    def test_float_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1.2, 2)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_dict_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle({"width": 1}, 2)
        self.assertEqual(str(context.exception), "width must be an integer")
        

if __name__ == '__main__':
    unittest.main()
