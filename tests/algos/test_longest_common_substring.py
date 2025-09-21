"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.longest_common_substring import longest_common


class LongestCommonSubstringTestCase(unittest.TestCase):

    def test_1(self):
        s1 = "amar"
        s2 = "tmak"
        assert longest_common(s1=s1, s2=s2) == 2

    def test_2(self):
        s1 = "amark"
        s2 = "kamar"
        assert longest_common(s1=s1, s2=s2) == 4


if __name__ == "__main__":
    unittest.main()