"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.hotel_trips_min_penalty import min_penalty


class MinPenaltyHotelTripTestCase(unittest.TestCase):

    def test_1(self):
        hotels_distances = [100, 200, 300, 400, 500]
        assert min_penalty(hotels_distances=hotels_distances, max_dist_day_trip=200) == 10000

    def test_2(self):
        hotels_distances = [110, 150, 200, 300, 400]
        assert min_penalty(hotels_distances=hotels_distances, max_dist_day_trip=200) == 0

    def test_3(self):
        hotels_distances = [110, 150, 190, 300, 390]
        assert min_penalty(hotels_distances=hotels_distances, max_dist_day_trip=200) == 100


if __name__ == "__main__":
    unittest.main()