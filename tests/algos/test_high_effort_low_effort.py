import unittest

from algos.high_effort_low_effort import high_low_effort_recursive
from algos.high_effort_low_effort import high_low_effort_recursive_dp
from algos.high_effort_low_effort import high_low_effort_using_just_dp

class HighLowIntensityTestCase(unittest.TestCase):

    def test_1(self):
        assert high_low_effort_recursive(low=[1, 5, 4, 5, 3], high=[3, 6, 8, 7, 6], n=5) == 20
        assert high_low_effort_recursive_dp(low=[1, 5, 4, 5, 3], high=[3, 6, 8, 7, 6], n=5) == 20
        # assert high_low_effort_using_just_dp(low=[1, 5, 4, 5, 3], high=[3, 6, 8, 7, 6], n=5) == 18
        assert high_low_effort_using_just_dp(low=[1, 2, 4, 5, 3], high=[3, 25, 8, 7, 6], n=5) == 20