"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.longest_palindromic_subsequence import longest_palindromic


class MaxProfitRestaurantsBuildTestCase(unittest.TestCase):

    def test_1(self):
        str_arr = ["t", "a", "t", "a", "t"]
        assert longest_palindromic(str_arr=str_arr) == 5

    def test_2(self):
        str_arr = ["b", "b", "a", "b"]
        assert longest_palindromic(str_arr=str_arr) == 3

if __name__ == "__main__":
    unittest.main()