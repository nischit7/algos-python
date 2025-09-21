"""
Tests for quick_sort.py.
"""

import unittest

from algos.coin_change import coin_change_recursive
from algos.coin_change import coin_change_with_repitition


class CoinChangeTestCase(unittest.TestCase):

    def test_1(self):
        assert coin_change_with_repitition(coins=[1, 2, 5], amount=11) == 3

    def test_1_1(self):
        assert coin_change_with_repitition(coins=[1, 2, 3], amount=11) == 4

    def test_2(self):
        assert coin_change_with_repitition(coins=[2], amount=3) == -1

    def test_3(self):
        assert coin_change_with_repitition(coins=[1], amount=0) == 0

    def test_4(self):
        assert coin_change_recursive(coins=[1, 2, 5, 10], amount=27) == 4

    def test_5(self):
        assert coin_change_recursive(coins=[83, 186, 408, 419], amount=6249) == 20

    def test_6(self):
        assert coin_change_recursive(coins=[3, 7, 405, 436], amount=8839) == 25

if __name__ == "__main__":
    unittest.main()