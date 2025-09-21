"""
Tests for quick_sort.py.
"""

import unittest

from algos.knapsack_with_repitition import max_value


class KnapsackWithRepitionTestCase(unittest.TestCase):

    def test_1(self):
        assert max_value(weights=[6, 3, 4, 2], values=[30, 14, 16, 9], target_weight=10) == 48



if __name__ == "__main__":
    unittest.main()