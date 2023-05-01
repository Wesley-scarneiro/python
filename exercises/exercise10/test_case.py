from typeValidation import TypeValidation
import unittest

class TestTypeValidation(unittest.TestCase):

    def test_validation_int(self):
        self.assertTrue(TypeValidation.validation("int", 10))
        self.assertFalse(TypeValidation.validation("int", 10.0))
        self.assertFalse(TypeValidation.validation("int", 3+2j))
        self.assertFalse(TypeValidation.validation("int", "string"))
        self.assertFalse(TypeValidation.validation("int", False))
        self.assertFalse(TypeValidation.validation("INT", 10))

    def test_validation_float(self):
        self.assertTrue(TypeValidation.validation("float", 10.0))
        self.assertFalse(TypeValidation.validation("float", 10))
        self.assertFalse(TypeValidation.validation("float", 3+2j))
        self.assertFalse(TypeValidation.validation("float", "string"))
        self.assertFalse(TypeValidation.validation("float", False))
        self.assertFalse(TypeValidation.validation("FLOAT", 10.0))
    
    def test_validation_complex(self):
        self.assertTrue(TypeValidation.validation("complex", 10+5j))
        self.assertFalse(TypeValidation.validation("complex", 10.0))
        self.assertFalse(TypeValidation.validation("complex", 3))
        self.assertFalse(TypeValidation.validation("complex", "string"))
        self.assertFalse(TypeValidation.validation("complex", False))
        self.assertFalse(TypeValidation.validation("COMPLEX", 10+5j))
    
    def test_validation_str(self):
        self.assertTrue(TypeValidation.validation("str", "string"))
        self.assertFalse(TypeValidation.validation("str", 10.0))
        self.assertFalse(TypeValidation.validation("str", 3+2j))
        self.assertFalse(TypeValidation.validation("str", 10))
        self.assertFalse(TypeValidation.validation("str", False))
        self.assertFalse(TypeValidation.validation("STR", "string"))

    def test_validation_bool(self):
        self.assertTrue(TypeValidation.validation("bool", False))
        self.assertFalse(TypeValidation.validation("bool", 10.0))
        self.assertFalse(TypeValidation.validation("bool", 3+2j))
        self.assertFalse(TypeValidation.validation("bool", 10))
        self.assertFalse(TypeValidation.validation("bool", "string"))
        self.assertFalse(TypeValidation.validation("BOOL", False))

if __name__ == "__main__":
    unittest.main()

'''
python3 -m unittest -v
test_validation_bool (test_case1.TestTypeValidation) ... ok
test_validation_complex (test_case1.TestTypeValidation) ... ok
test_validation_float (test_case1.TestTypeValidation) ... ok
test_validation_int (test_case1.TestTypeValidation) ... ok
test_validation_str (test_case1.TestTypeValidation) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
'''