"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.multiply_oper_on_three_symbols import multiple_possible_recursive


class MaxProfitRestaurantsBuildTestCase(unittest.TestCase):

    def test_1(self):
        restaurants_distances = [100, 150, 210, 250, 350]
        target = "bbbbac"
        assert multiple_possible_recursive(restaurants_distances=restaurants_distances, profit_at_each_spot=None, min_dist_restaurants=100) == 50


if __name__ == "__main__":
    unittest.main()