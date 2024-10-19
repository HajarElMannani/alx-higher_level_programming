from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    def setUp(self):
        self.base = Base()

    def test_valid_init(self):
        base = Base()
        self.assertEqual(base.id, 2)
    def test_valid_init1(self):
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_valid_init2(self):
        base = Base(None)
        self.assertEqual(base.id, 5)
if __name__ == '__main__':
    unittest.main()
