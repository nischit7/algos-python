"""
Tests for quick_sort.py.
"""

import unittest

from algos.knapsack_without_repitition import max_value


class KnapsackWithRepitionTestCase(unittest.TestCase):

    def test_1(self):
        assert max_value(weights=[15, 12, 10, 5], values=[15, 10, 8, 1], target_weight=22) == 18

    def test_2(self):
        assert max_value(weights=[3, 4, 4, 6], values=[2, 3, 4, 1], target_weight=8) == 7


if __name__ == "__main__":
    unittest.main()