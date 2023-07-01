#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """
        Test for an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """
        Test for a list with a single element
        """
        self.assertEqual(max_integer([10]), 10)

    def test_ordered_list(self):
        """
        Test for a list with elements in ascending order
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """
        Test for a list with elements in random order
        """
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """
        Test for a list with negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_numbers(self):
        """
        Test for a list with floating-point numbers
        """
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)


if __name__ == '__main__':
    unittest.main()
