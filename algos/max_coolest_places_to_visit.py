import numpy as np

def max_coolest_places(places: list, cool_factor: list) -> int:
    dp = [0 for _ in range(len(places) + 1)]

    for i in range(1, len(places)):
        for j in range(0, i):
            if (places[i] - places[j]) < 300:
                if cool_factor[j] > cool_factor[i]:
                    dp[i] = cool_factor[j]
        if places[i] >= 300:
            dp[i] = dp[i] + cool_factor[i]

    return dp[len(cool_factor) - 1]