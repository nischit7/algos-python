import numpy as np

def min_fuel_stops(stations: np.ndarray, target_miles: int, starting_dist: int, starting_fuel: int):
    num_of_stops = len(stations)
    dp = np.zeros(shape=[num_of_stops + 1, 2])
    dp[0][0] = starting_fuel
    dp[0][1] = 0

    init_dist = starting_dist
    init_fuel = starting_fuel

    for curr_station_index in range(1, num_of_stops + 1):

        station_dist_from_start = stations[curr_station_index - 1][0]
        fuel_available = stations[curr_station_index - 1][1]

        for prev_station_index in range(curr_station_index):

            max_miles_possible_from_prev_station = dp[prev_station_index][0]
            no_of_stops_making_that_fuel = dp[prev_station_index][1]

            if dp[curr_station_index][0] != 0 and max_miles_possible_from_prev_station < station_dist_from_start:
                continue

            possible_stops = no_of_stops_making_that_fuel + 1
            possible_miles_possible = fuel_available + max_miles_possible_from_prev_station
            if possible_miles_possible >= target_miles:
                if dp[curr_station_index][1] > possible_stops:
                    dp[curr_station_index][1] = min(dp[curr_station_index][1], possible_stops)
                    dp[curr_station_index][0] = max(dp[curr_station_index][0], possible_miles_possible)
                else:
                    dp[curr_station_index][0] = max(dp[curr_station_index][0], possible_miles_possible)
                    dp[curr_station_index][1] = possible_stops
            else:
                dp[curr_station_index][0] = max(dp[curr_station_index][0], possible_miles_possible)
                dp[curr_station_index][1] = possible_stops

    for index in range(len(dp)):
        if dp[index][0] >= target_miles:
            return dp[index][1]

    return -1