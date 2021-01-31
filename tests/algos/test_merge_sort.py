"""
Tests for merge_sort.py.
"""

import unittest
import pytest

from algos.merge_sort import merge_sort

class MergeSortTestCase(unittest.TestCase):

    def test_sort_succeeds(self):
        unsort_lst = [64, 4, 2, 0, 5, 77, 8, 111, 76, 984, 3]
        assert merge_sort(unsort_lst=unsort_lst) == [0, 2, 3, 4, 5, 8, 64, 76, 77, 111, 984]

    def test_sort_fails_for_none(self):
        with pytest.raises(AssertionError):
            merge_sort(None)

    def test_sort_fails_for_empty_lst(self):
        with pytest.raises(AssertionError):
            merge_sort([])

    def test_sort_fails_for_non_integer(self):
        with pytest.raises(AssertionError):
            merge_sort([3, '1'])
