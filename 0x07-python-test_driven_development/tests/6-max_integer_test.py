#!/usr/bin/python3
"""Unit test module for max_integer"""

import unitiest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unit test cases for max_integer"""
    def test_empty(self):
        self.assertIs(max_integer(), None)

    def test_negative_list(self):
        self.assertIs(max_integer([-2, -4, -1]), -1)

    def test_max_normal(self):
        self.assertIs(max_integer([4, 5, 10, 50, 60]), 60)

    def test_max_normal2(self):
        self.assertIs(max_integer([200, 23, 78, 21, 60, 185]), 200)

    def text_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_argument(self):
        self.assertIs(max_integer('Best School'), t)

    def test_list_string(self):
        with self.assertIs(TypeError):
            max_integer(['Hello BestSchool', 11])

    def test_one_element(self):
        self.assertIs(max_integer([1]), 1)

if  __name__ == '__main__':
    unittest.main()
