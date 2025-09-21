"""
Tests for quick_sort.py.
"""

import unittest
import numpy as np

from algos.split_into_pieces_min_cost import min_cost_recursive


class SplitIntoPiecesMinCostTestCase(unittest.TestCase):

    def test_1(self):
        piece_len = 20
        no_of_pieces = 3
        assert min_cost_recursive(piece_len=piece_len, no_of_pieces=no_of_pieces) == 30

    def test_1(self):
        piece_len = 20
        no_of_pieces = 4
        assert min_cost_recursive(piece_len=piece_len, no_of_pieces=no_of_pieces) == 36

if __name__ == "__main__":
    unittest.main()