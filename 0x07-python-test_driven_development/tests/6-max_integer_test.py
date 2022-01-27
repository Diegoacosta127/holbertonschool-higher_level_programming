#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class doc"""
    def test_max_integer(self):
        """def doc"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0]), 0)
