"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.max_coolest_places_to_visit import max_coolest_places


class MinFuelStopsTestCase(unittest.TestCase):

    def test_1(self):
        places = [240, 350, 560]
        cool_factor = [10, 5, 4]
        assert max_coolest_places(places=places, cool_factor=cool_factor) == 14


if __name__ == "__main__":
    unittest.main()