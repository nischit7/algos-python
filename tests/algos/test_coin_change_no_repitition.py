"""
Tests for quick_sort.py.
"""

import unittest

from algos.coin_change_no_repitition import coin_change_no_repitition


class CoinChangeTestCase(unittest.TestCase):

    def test_1(self):
        assert coin_change_no_repitition(coins=[1, 2, 5], amount=11) == False

    def test_2(self):
        assert coin_change_no_repitition(coins=[1, 2, 5], amount=8) == True

    def test_3(self):
        assert coin_change_no_repitition(coins=[1, 5, 10, 20], amount=31) == True

    def test_4(self):
        assert coin_change_no_repitition(coins=[20, 5, 10, 1], amount=40) == False


if __name__ == "__main__":
    unittest.main()