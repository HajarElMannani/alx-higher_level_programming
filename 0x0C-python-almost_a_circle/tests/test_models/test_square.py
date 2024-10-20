#!/usr/bin/python3
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestInitSquare(unittest.TestCase):

    def test_one_argument(self):
        s1 = Square(5)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 0/0 - 5")
    
    def test_two_aruments(self):
        s2 = Square(2, 2)
        self.assertEqual(str(s2), f"[Square] ({s2.id}) 2/0 - 2")

    def test_three_arguments(self):
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), f"[Square] ({s3.id}) 1/3 - 3")

    def test_four_arguments(self):
        s4 = Square(5, 3, 1, 7)
        self.assertEqual(str(s4), f"[Square] (7) 3/1 - 5")

    def test_more_five_arguments(self):
        with self.assertRaises(TypeError):
            Square(5, 3, 1, 1, 8)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_isinstance_rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_isinstance_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_get_size(self):
        s1 = Square(2, 1, 3, 4).size
        self.assertEqual(s1, 2)

    def test_set_size(self):
        s2 = Square(1, 2, 3, 4)
        s2.size = 5
        self.assertEqual(s2.size, 5)

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3, 1, 3, 2)

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2, 2, 4)

    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("some")

    def test_size_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_no_size(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.2)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2])

    def test_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"d": 5})

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2))

    def test_size_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_large_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1e360)
            
    def test_get_width(self):
        s1 = Square(1, 2, 5, 4).width
        self.assertEqual(s1, 1)
        
    def test_set_width(self):
        s2 = Square(2, 1, 3, 4)
        s2.size = 6
        self.assertEqual(s2.width, 6)

    '''test x attribute'''

    def test_get_x_default(self):
        s1 = Square(2)
        self.assertEqual(s1.x, 0)

    def test_get_x(self):
        s2 = Square(2, 1, 3, 5)
        self.assertEqual(s2.x, 1)

    def test_set_x(self):
        s3 = Square(2, 1, 3, 5)
        s3.x = 4
        self.assertEqual(s3.x, 4)

    def test_get_x_default(self):
        s1 = Square(5)
        self.assertEqual(s1.y, 0)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -3)

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "some")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 2.4)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [1, 2])

    def test_x_dictionnary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"d": 3})

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1,))

    def test_x_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True)

    def test_x_large(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 1e350)

    '''test y attribute'''
    
    def test_get_y(self):
        s3 = Square(2, 4, 5, 6)
        self.assertEqual(s3.y, 5)
    
    def test_set_y(self):
        s3 = Square(2, 1, 3, 5)
        s3.y = 9
        self.assertEqual(s3.y, 9)

    def test_get_y_default(self):
        s1 = Square(6)
        self.assertEqual(s1.y, 0)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 3, -2)

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, None)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, "some")
    
    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, 2.4)

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, [1, 2])

    def test_y_dictionnary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, {"d": 3})

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, (1,))

    def test_y_boolean(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, True)
            
    def test_y_large(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1e350)
        
            
    def test_get_height(self):
        s1 = Square(1, 2, 4, 6).height
        self.assertEqual(s1, 1)
        
    def test_size_private(self):
        with self.assertRaises(AttributeError):
            s1 = Square(1, 5, 2, 7).__size        
            print(s1)

class TestAreaSquare(unittest.TestCase):
    '''test the are module'''
    def test_area_square(self):
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_area_long(self):
        r2 = Square(999999999999999, 0)
        self.assertEqual(r2.area(), 999999999999998000000000000001)

    def test_change(self):
        r3 = Square(3, 0, 0, 2)
        r3.size = 5
        self.assertEqual(r3.area(), 25)


    def test_only_one(self):
        r4 = Square(2, 4, 0, 1)
        with self.assertRaises(TypeError):
            r4.area(1)

class TestDisplaySquare(unittest.TestCase):

    def test_display_square(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r1 = Square(4, 0, 0, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        expected = ("####\n####\n####\n####\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display1_square(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r2 = Square(1, 0, 0, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        expected = ("#\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display_x_square(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r3 = Square(3, 1, 0, 0)
        r3.display()
        sys.stdout = sys.__stdout__
        expected = (" ###\n ###\n ###\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display_y_square(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r4 = Square(3, 0, 1, 0)
        r4.display()
        sys.stdout = sys.__stdout__
        expected = ("\n###\n###\n###\n")
        self.assertEqual(cap_output.getvalue(), expected)

    def test_display_all_square(self):
        cap_output = StringIO()
        sys.stdout = cap_output
        r5 = Square(2, 3, 2, 0)
        r5.display()
        sys.stdout = sys.__stdout__
        expected = ("\n\n   ##\n   ##\n")
        self.assertEqual(cap_output.getvalue(), expected)
        
    def test_display_one_argmnt_Square(self):
        r6 = Rectangle(3, 2, 5, 7, 3)
        with self.assertRaises(TypeError):
            r6.display(1)


class TestStrSquare(unittest.TestCase):
    '''test __str__method'''
    def test_str_square(self):
        s1 = Square(4)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 0/0 - 4")

    def test_str_change_arg_square(self):
        s2 = Square(7, 0, 0, [3])
        s2.width = 2
        s2.x = 3
        s2.y = 8
        self.assertEqual(str(s2), f"[Square] ([3]) 3/8 - 2")

    def test_str_square(self):
         s3 = Square(5, 5, 0, 2)
         self.assertEqual(str(s3), f"[Square] (2) 5/0 - 5")

    def test_str_one_arg_square(self):
        s = Square(5, 0, 3, 1)
        with self.assertRaises(TypeError):
            s.__str__(1)

class TestUpdateSquare(unittest.TestCase):

    def test_update_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")

    def test_update_Nothing_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update()
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        
    def test_update_two_args_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")

    def test_update_three_args_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")


    def test_update_four_args_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_five_args_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 4, 5)
        self.assertEqual(str(s1), "[Square] (89) 4/5 - 2")

    def test_update_six_args_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 4, 5, 6)
        self.assertEqual(str(s1), "[Square] (89) 4/5 - 2")

    def test_update_two_times_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3, 5)
        s1.update(6, 2, 7, 2)
        self.assertEqual(str(s1), "[Square] (6) 7/2 - 2")
    
    def test_update_None_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(None)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 10/10 - 10")

    def test_update_None_id_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(None, 2, 3, 4)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 3/4 - 2")

    def test_update_size_zero(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(3, 0)

    def test_update__str_size(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(3, "be")

    def test_update_negative_size(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(3, -2)

    def test_update_negative_x_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(3, 1,-2)

    def test_update_str__x_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(3, 4, "be")

    def test_update_negative_y_sqare(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(3, 4, 2, -3)

    def test_update_str_y_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(3, 4, 2, "be")

class TestUpdateKwargsSquare(unittest.TestCase):
     
    def test_update_kwargs_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(id=1)
        self.assertEqual(str(s1), "[Square] (1) 10/10 - 10")

    def test_update_two_kwargs_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(size=1, x=2, id=10)
        self.assertEqual(str(s1), "[Square] (10) 2/10 - 1")

    def test_update_three_kwargs_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(s1), "[Square] (89) 3/1 - 2")

    def teat_update_four_kwargs_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(x=1, y=3, size=4, id=89)
        self.assertEqual(str(s1), "[Square] (89) 1/3 - 4")

    def test_update_kwargs_id_None_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(id=None, size=2, y=1)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 10/1 - 2")

    def test_update_kwargs_None_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(None)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 10/10 - 10")

    def test_update_kwargs_two_times_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(id=2, x=3)
        s1.update(y=5, size=4)
        self.assertEqual(str(s1), f"[Square] (2) 3/5 - 4")
        
    def test_update_size_zero_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(size=0)

    def test_update_kwargs_str_size(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size="hol")

    def test_update_kwargs_negative_size(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(size=-2)

    def test_update_kwargs_negative_x_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(x=-2)

    def test_update_kwargs_str_x_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x="hol")

    def test_update_kwargs_negative_y_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(y=-3)

    def test_update_kwargs_str_y_square(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y="hol")

    def test_update_kwargs_wrong_keys_square(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(size=2, id=1, l=9, m=5, y=6, x=4)
        self.assertEqual(str(s1), "[Square] (1) 4/6 - 2")

    def test_update_args_kwargs_squqre(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(2, 1, size=5, x=3)
        self.assertEqual(str(s1), "[Square] (2) 10/10 - 1")

class TestToDictionarySquare(unittest.TestCase):

    def test_to_dictionary_Square(self):
        s1 = Square(10, 2, 1, 2)
        s1_dict = s1.to_dictionary()
        self.assertDictEqual(s1_dict, {'x': 2, 'y': 1, 'id': 2, 'size': 10})
        #test type

    def test_to_dictionary_one_argument_s(self):
        s1 = Square(10, 1, 9, 3)
        with self.assertRaises(TypeError):
            s1.to_dictionary(1)

    def test_to_dictionary_update_Square(self):
        s1 = Square(10, 1, 9, 3)
        s2 = Square(3, 5, 2, 9)
        s2.update(**s1.to_dictionary())
        self.assertFalse(s1 == s2)
        

if __name__ == '__main__':
    unittest.main()
