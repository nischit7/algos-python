
def max_value(weights: list, values: list, target_weight: int) -> int:

    dp = [0] * (target_weight + 1)

    for mini_target_weight in range(1, target_weight + 1):
        max_so_far = 0
        for index in range(0, len(weights)):
            if weights[index] <= mini_target_weight:
                max_so_far = max(max_so_far, dp[mini_target_weight - weights[index]] + values[index])
        dp[mini_target_weight] = max_so_far

    return dp[len(dp) - 1]