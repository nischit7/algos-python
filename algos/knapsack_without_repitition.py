import numpy as np


def max_value(weights: list, values: list, target_weight: int) -> int:

    dp = np.zeros((len(weights) + 1, target_weight + 1), dtype=int)

    for mini_target_weight in range(1, target_weight + 1):
        for index in range(0, len(weights)):
            dp_index = index + 1
            if weights[index] <= mini_target_weight:
                # dp[i, k] = max(dp[i - 1, k], val[i] + dp[i - 1, mini_target_weight - weight[i]])
                dp[dp_index, mini_target_weight] = max(dp[dp_index - 1, mini_target_weight], values[index] + dp[dp_index - 1, mini_target_weight - weights[index]])
            else:
                dp[dp_index, mini_target_weight] = dp[dp_index - 1, mini_target_weight]

    return dp[len(weights), target_weight]