#!/usr/bin/python3

"""
An example of quick sort.
"""

import sys
import logging as log


def quick_sort(unsort_lst: []) -> []:
    """
    Sorts as per quick sort algo.

    :param unsort_lst: Unsorted list of integer
    :return: sorted list of integer
    """

    assert unsort_lst is not None, 'The input list should be a valid collection of integers'

    if len(unsort_lst) <= 1:
        return unsort_lst

    assert len(unsort_lst) >= 1, 'The input list should be a minimum size of 1'
    assert all(isinstance(x, int) for x in unsort_lst),\
        'The input list should be a collection of integer'

    # Choosing the last element as the pivot
    pivot_index = len(unsort_lst) - 1
    pivot_value = unsort_lst[pivot_index]

    left_lst = []
    right_lst = []
    for index in range(0, len(unsort_lst) - 1):
        if unsort_lst[index] < pivot_value:
            left_lst.append(unsort_lst[index])
        else:
            right_lst.append(unsort_lst[index])

    pivot_left_lst = quick_sort(unsort_lst=left_lst)
    pivot_right_lst = quick_sort(unsort_lst=right_lst)

    return _merge(pivot_left_lst, pivot_right_lst, pivot_value)


def _merge(left_lst: [], right_lst: [], pivot_value: int) -> []:
    merged_lst = []
    merged_lst.extend(left_lst)
    merged_lst.append(pivot_value)
    merged_lst.extend(right_lst)
    return merged_lst

if __name__ == '__main__':
    ROOT = log.getLogger()
    ROOT.setLevel(log.INFO)
    HANDLER = log.StreamHandler(sys.stderr)
    HANDLER.setLevel(log.INFO)
    FORMATTER = log.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    HANDLER.setFormatter(FORMATTER)
    ROOT.addHandler(HANDLER)

    UNSORTED_LST = [99, 4, 11, 0, 5, 888, 2, 8, 889, 111, 333, 3]
    log.info("The unsorted list '%s'", UNSORTED_LST)
    log.info("The list after sorting")
    log.info(quick_sort(unsort_lst=UNSORTED_LST))
