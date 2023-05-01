import unittest

class TypeValidation(unittest.TestCase):

    @staticmethod
    def integer(value: int):
        if isinstance(value, int):
            return True
        else:
            raise TypeError(f"Type '{type(value)}' invalid")


