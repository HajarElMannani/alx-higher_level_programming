#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(1, 1, 0, 0, None)

   # def test_valid_init(self):
    #    rectangle = Rectangle(10, 2)
     #   self.assertEqual(rectangle.id, 5)

    def test_valid_init1(self):
        rectangle = Rectangle(2, 10)
        self.assertEqual(rectangle.id, 3)

    def	test_valid_init1(self):
        rectangle = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rectangle.id, 12)


class TestHeight(unittest.TestCase):

    def test_negative_heiht(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, -2)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_zero_height(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(3, 0)
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


    def test_zero_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)
        self.assertEqual(str(context.exception), "width must be > 0")
        
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
        

class TestX(unittest.TestCase):

    def test_negative_x(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, -1)
        self.assertEqual(str(context.exception), "x must be >= 0")
 

    def test_string_x(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(5, 3, "me")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_None_x(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(3, 1, None)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_list_x(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(4, 1, [1, 2])
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_tuple_x(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 1, (1,))
        self.assertEqual(str(context.exception), "x must be an integer")
        
    def test_float_x(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 1, 0.2)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_dict_x(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 1, {"x": 1})
        self.assertEqual(str(context.exception), "x must be an integer")

class TestY(unittest.TestCase):

    
    def test_negative_y(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 1, 1, -2)
        self.assertEqual(str(context.exception), "y must be >= 0")


    def test_string_y(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(5, 1, 1, "de")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_None_y(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(3, 1, 1, None)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_list_y(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(4, 1, 1, [1, 2])
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_tuple_y(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 1, 1, (1,))
        self.assertEqual(str(context.exception), "y must be an integer")
        
    def test_float_y(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 1, 1, 3.2)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_dict_y(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 1, 1, {"height": 1})
        self.assertEqual(str(context.exception), "y must be an integer")

class TestArea(unittest.TestCase):
    '''test the are module'''
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area_long(self):
        r2 = Rectangle(999999999999999, 9999999999999998)
        self.assertEqual(r2.area(), 9999999999999988000000000000002)

    def test_change(self):
        r3 = Rectangle(3, 2, 0, 1, 1)
        r3.width = 5
        r3.height = 4
        self.assertEqual(r3.area(), 20)


    def test_only_one(self):
        r4 = Rectangle(2, 4)
        with self.assertRaises(TypeError):
            r4.area(1)


class TestDisplay(unittest.TestCase):

    def test_display(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        expected = ("####\n####\n####\n####\n####\n####\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display1(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r2 = Rectangle(1, 3, 0, 0, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        expected = ("#\n#\n#\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display_x(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r3 = Rectangle(3, 2, 1, 0)
        r3.display()
        sys.stdout = sys.__stdout__
        expected = (" ###\n ###\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display_y(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r4 = Rectangle(3, 2, 0, 1, 0)
        r4.display()
        sys.stdout = sys.__stdout__
        expected = ("\n###\n###\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display_all(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r5 = Rectangle(2, 3, 3, 2, 0)
        r5.display()
        sys.stdout = sys.__stdout__
        expected = ("\n\n   ##\n   ##\n   ##\n")
        self.assertEqual(cap_output.getvalue(), expected)
        
    def test_display_one_argmnt(self):
        r6 = Rectangle(3, 2, 5, 7, 3)
        with self.assertRaises(TypeError):
            r6.display(1)

        
class TestStr(unittest.TestCase):
    '''test __str__method'''
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_change_arg(self):
        r2 = Rectangle(7, 7, 0, 0, [3])
        r2.width = 2
        r2.height = 5
        r2.x = 3
        r2.y = 8
        self.assertEqual(str(r2), "[Rectangle] ([3]) 3/8 - 2/5")

    def test_str(self):
         r3 = Rectangle(5, 5, 1, 0, 2)
         self.assertEqual(str(r3), "[Rectangle] (2) 1/0 - 5/5")

    def test_str_one_arg(self):
        r = Rectangle(5, 7, 0, 3, 1)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestUpdate(unittest.TestCase):

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_four_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_five_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_six_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_two_times(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        r1.update(6, 2, 4, 7, 2)
        self.assertEqual(str(r1), "[Rectangle] (6) 7/2 - 2/4")
    
    def test_update_None(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(None)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/10")

    def test_update_None_id(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(None, 2, 3, 4)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 4/10 - 2/3")
        
    def test_update_width_zero(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(3, 0)

    def test_update__str_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(3, "be")

    def test_update_negative_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(3, -2)

    def test_update_height_zero(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(3, 2, 0)

    def test_update_str_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(3, 1, "be")

    def test_update_negative_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(3, 1, -2)

    def test_update_negative_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(3, 1, 5, -2)

    def test_update_str__x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(3, 4, 2, "be")

    def test_update_negative_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(3, 4, 2, 4, -3)

    def test_update_str_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(3, 4, 2, 1, "be")

class TestUpdateKwargs(unittest.TestCase):

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_two_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2, id=10)
        self.assertEqual(str(r1), "[Rectangle] (10) 2/10 - 1/10")

    def test_update_three_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")

    def teat_update_four_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_kwargs_id_None_(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=None, height=3, y=1)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/1 - 10/3")

    def test_update_kwargs_None(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(None)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/10")

    def test_update_kwargs_two_times(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=2, x=3, height=1)
        r1.update(y=5, height=7, width=4)
        self.assertEqual(str(r1), f"[Rectangle] (2) 3/5 - 4/7")
        
    def test_update_width_zero(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(width=0)

    def test_update_kwargs_str_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width="hol")

    def test_update_kwargs_negative_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(width=-2)

    def test_update_height_zero(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(height=0)

    def test_update_kwargs_str_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height="hol")

    def test_update_kwargs_negative_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(height=-3)

    def test_update_kwargs_negative_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-2)

    def test_update_kwargs_str_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x="hol")

    def test_update_kwargs_negative_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(y=-3)

    def test_update_kwargs_str_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y="hol")

    def test_update_kwargs_wrong_keys(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(width=2, id=1, l=9, m=5, y=6, x=4)
        self.assertEqual(str(r1), "[Rectangle] (1) 4/6 - 2/10")

    def test_update_args_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(2, 1, width=5, x=3)
        self.assertEqual(str(r1), "[Rectangle] (2) 10/10 - 1/10")

class TestToDictionary(unittest.TestCase):

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 3)
        r1_dict = r1.to_dictionary()
        self.assertDictEqual(r1_dict, {'x': 1, 'y': 9, 'id': 3, 'height': 2, 'width': 10})
        #if dictionary

    def test_to_dictionary_one_argument(self):
        r1 = Rectangle(10, 2, 1, 9, 3)
        with self.assertRaises(TypeError):
            r1.to_dictionary(1)

    def test_to_dictionary_update(self):
        r1 = Rectangle(10, 2, 1, 9, 3)
        r2 = Rectangle(3, 7, 5, 2, 9)
        r2.update(**r1.to_dictionary())
        self.assertFalse(r1 == r2)
        

    
if __name__ == '__main__':
    unittest.main()         
