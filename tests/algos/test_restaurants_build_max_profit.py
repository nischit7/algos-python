"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.restaurants_build_max_profit import max_profit


class MaxProfitRestaurantsBuildTestCase(unittest.TestCase):

    def test_1(self):
        restaurants_distances = [100, 150, 210, 250, 350]
        profit = [10, 10, 20, 10, 20]
        assert max_profit(restaurants_distances=restaurants_distances, profit_at_each_spot=profit, min_dist_restaurants=100) == 50

    def test_2(self):
        restaurants_distances = [100, 150, 210, 250, 350]
        profit = [10, 30, 20, 30, 20]
        assert max_profit(restaurants_distances=restaurants_distances, profit_at_each_spot=profit, min_dist_restaurants=100) == 80

    def test_3(self):
        restaurants_distances = [100, 150, 210, 250, 350]
        profit = [10, 30, 20, 40, 40]
        assert max_profit(restaurants_distances=restaurants_distances, profit_at_each_spot=profit, min_dist_restaurants=100) == 110


if __name__ == "__main__":
    unittest.main()