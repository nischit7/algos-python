#!/usr/bin/env python3

"""
An example of merge sort.
"""

import sys
import logging as log


def merge_sort(unsort_lst: []) -> []:
    """
    Utilizes merge sort algo to sort the array of integers.

    :param unsort_lst: The unsorted collection of int
    :return: sorted list
    """

    assert unsort_lst is not None, 'The input list should be a valid collection of integers'
    assert len(unsort_lst) >= 1, 'The input list should be a minimum size of 1'
    assert all(isinstance(x, int) for x in unsort_lst),\
        'The input list should be a collection of integer'

    unsort_lst_len = len(unsort_lst)
    if unsort_lst_len == 1:
        return unsort_lst

    left_lst_len = int(unsort_lst_len / 2)

    left_lst = unsort_lst[0:left_lst_len]
    right_lst = unsort_lst[left_lst_len:]

    left_merge_sort_lst = merge_sort(left_lst)
    right_merge_sort_lst = merge_sort(right_lst)

    merged_lst = _merge(left_lst=left_merge_sort_lst, right_lst=right_merge_sort_lst)
    return merged_lst


def _merge(left_lst: [], right_lst: []) -> []:
    """

    :param left_lst: Sorted left side of the list
    :param right_lst: Sorted right side of the list
    :return: After a sorted list after merging the left and right lists
    """
    merged_lst = []
    left_pos = 0
    merged_lst.extend(right_lst)

    # Add remaining from left
    for left_index in range(left_pos, len(left_lst)):
        for merge_index in range(0, len(merged_lst)): # pylint: disable=C0200
            if left_lst[left_index] < merged_lst[merge_index]:
                merged_lst.insert(merge_index, left_lst[left_index])
                left_pos = left_pos + 1
                break

    # Add remaining from left
    for left_index in range(left_pos, len(left_lst)):
        merged_lst.append(left_lst[left_index])

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
    log.info(merge_sort(unsort_lst=UNSORTED_LST))
