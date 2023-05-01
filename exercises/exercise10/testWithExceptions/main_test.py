import unittest

def main():
    suite = unittest.TestLoader().discover("exercise10/testWithExceptions")
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

'''
test_integer_int (teste_case.TestCatchExceptions) ... ok
test_integer_invalid (teste_case.TestCatchExceptions) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
'''