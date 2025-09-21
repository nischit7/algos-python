import unittest

from algos.max_points_from_cards import max_points_from_cards_recursive
from algos.high_effort_low_effort import high_low_effort_recursive_dp

class MaxPointsFromCardsTestCase(unittest.TestCase):

    def test_1(self):
        assert max_points_from_cards_recursive(cards=[1, 2, 3, 4, 5, 6, 1], max_cards_to_take=3) == 12
        assert max_points_from_cards_recursive(cards=[2, 2, 2], max_cards_to_take=2) == 4
        assert max_points_from_cards_recursive(cards=[9, 7, 7, 9, 7, 7, 9], max_cards_to_take=7) == 55