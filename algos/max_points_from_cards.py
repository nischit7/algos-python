import numpy as np

# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
#
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
#
# Your score is the sum of the points of the cards you have taken.
#
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
def max_points_from_cards_recursive(cards: list, max_cards_to_take: int) -> int:

    left_card = cards[0]
    right_card = cards[len(cards) - 1]

    return max(
        left_card + max_points_from_cards_recursive_without_dp(cards=cards, max_cards_to_take=max_cards_to_take - 1, start=1, end=len(cards) - 1),
        right_card + max_points_from_cards_recursive_without_dp(cards=cards, max_cards_to_take=max_cards_to_take - 1, start=0, end=len(cards) - 2))

def max_points_from_cards_recursive_without_dp(cards: list, max_cards_to_take: int, start: int, end: int) -> int:

    if max_cards_to_take <= 0:
        return 0

    left_card = cards[start]
    right_card = cards[end]

    max_points = max(
        left_card + max_points_from_cards_recursive_without_dp(cards=cards, max_cards_to_take=max_cards_to_take - 1, start=start + 1, end=end),
        right_card + max_points_from_cards_recursive_without_dp(cards=cards, max_cards_to_take=max_cards_to_take - 1, start=start, end=end - 1))

    return max_points