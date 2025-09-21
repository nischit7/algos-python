# Yuckdonald’s is considering opening a series of restaurants along Quaint Valley Highway (QVH).
# The n possible locations are along a straight line, and the distances of these locations from the start of QVH are,
# in miles and in increasing order, m1, m2, . . . , mn. The constraints are as follows:
# r At each location, Yuckdonald’s may open at most one restaurant.
#   The expected profit from opening a restaurant at location i is pi , where pi > 0 and i = 1,2,...,n.
# r Any two restaurants should be at least k miles apart, where k is a positive integer.
# Give an efficient algorithm to compute the maximum expected total profit subject to the given constraints.


import numpy as np

def max_profit(restaurants_distances: list, profit_at_each_spot: [], min_dist_restaurants) -> int:

    hotel_len = len(restaurants_distances)
    # Base case
    t = [0] * (hotel_len + 1)
    t[0] = 0

    if restaurants_distances[0] > min_dist_restaurants:
        return []

    for i in range(1, hotel_len + 1):
        restaurant_i_index = i - 1
        restaurant_dist_to_i = restaurants_distances[restaurant_i_index]
        profit = profit_at_each_spot[restaurant_i_index]

        for j in range(0, i):
            restaurant_j_index = j - 1
            restaurant_dist_to_j = restaurants_distances[restaurant_j_index] if restaurant_j_index >= 0 else 0
            restaurant_dist = restaurant_dist_to_i - restaurant_dist_to_j

            if restaurant_dist < min_dist_restaurants:
                continue

            t[i] = max(t[i], t[j] + profit)

    return t[len(t) - 1]