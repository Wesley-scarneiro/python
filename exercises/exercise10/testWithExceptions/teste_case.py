import unittest
from catchExceptions import TypeValidation

class TestCatchExceptions(unittest.TestCase):

    def test_integer_int(self):
        self.assertTrue(TypeValidation.integer(10))
    
    def test_integer_invalid(self):
        self.assertRaises(TypeError, TypeValidation.integer, 10.0)


if __name__ == "__main__":
    unittest.main()