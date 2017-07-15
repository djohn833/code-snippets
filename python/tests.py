import doctest
import unittest
import utils


class TestDocstrings(unittest.TestCase):
    def test_utils(self):
        result = doctest.testmod(utils)
        self.assertEqual(result.failed, 0)


if __name__ == '__main__':
    unittest.main()
