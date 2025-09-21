"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.min_fuel_stops import min_fuel_stops


class MinFuelStopsTestCase(unittest.TestCase):

    def test_1(self):
        stations = [
            [10, 60],
            [20, 30],
            [30, 30],
            [60, 40]]
        assert min_fuel_stops(stations=np.array(stations), target_miles=100, starting_dist=10, starting_fuel=10) == 2

    def test_2(self):
        stations = [
            [10, 30],
            [20, 30],
            [30, 60],
            [60, 40]]
        assert min_fuel_stops(stations=np.array(stations), target_miles=100, starting_dist=10, starting_fuel=10) == 2


if __name__ == "__main__":
    unittest.main()