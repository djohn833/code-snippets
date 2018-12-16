import doctest
import unittest
import utils

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite('regex_helpers'))
    tests.addTests(doctest.DocTestSuite('utils'))
    return tests

if __name__ == '__main__':
    unittest.main()
