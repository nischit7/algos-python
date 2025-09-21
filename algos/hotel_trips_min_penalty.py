# You are going on a long trip. You start on the road at mile post 0. Along the way there are n hotels,
# at mile posts a1 < a2 < ··· < an, where each ai is measured from the starting point.
# The only places you are allowed to stop are at these hotels, but you can choose which of the hotels you stop at.
# You must stop at the final hotel (at distance an), which is your destination.
# You’d ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing of the hotels).
# If you travel x miles during a day, the penalty for that day is (200 − x)2.
# You want to plan your trip so as to minimize the total penalty—that is, the sum, over all travel days,
# of the daily penalties. Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.


import numpy as np

def min_penalty(hotels_distances: list, max_dist_day_trip: 200) -> int:

    hotel_len = len(hotels_distances)
    # Base case
    t = [float("inf")] * (hotel_len + 1)
    t[0] = 0

    if hotels_distances[0] > max_dist_day_trip:
        return []

    for i in range(1, hotel_len + 1):
        hotel_i_index = i - 1
        hotel_dist_to_i = hotels_distances[hotel_i_index]
        # dist_from_prev_stop = hotel_dist_to_i - hotels_distances[hotel_i_index - 1] if hotel_i_index - 1 >= 0 else 0
        # curr_hotel_not_skipped = (max_dist_day_trip - dist_from_prev_stop) * (max_dist_day_trip - dist_from_prev_stop)
        # curr_hotel_when_skipped = t[i - 1]
        # t[i] = min(curr_hotel_not_skipped, curr_hotel_when_skipped)

        for j in range(0, i):
            hotel_j_index = j - 1
            hotel_dist_to_j = hotels_distances[hotel_j_index] if hotel_j_index >= 0 else 0
            hotel_dist = hotel_dist_to_i - hotel_dist_to_j

            if hotel_dist > 200:
                continue

            # penalty = (200 - x)^2
            penalty = (max_dist_day_trip - hotel_dist) * (max_dist_day_trip - hotel_dist)
            t[i] = min(t[i], t[j] + penalty)

    return t[len(t) - 1]