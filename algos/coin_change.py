import numpy as np
import sys
def coin_change_recursive(coins: list, amount: int) -> int:

    if coins is None or len(coins) == 0:
        return -1

    if amount == 0:
        return 0

    all_coins = coins.copy()

    ind_amt = 0
    min_coin_matching_amt = 0
    min_coin_count_for_that_amt_so_far = float('inf')
    for coin in coins:

        if amount == coin:
            return 1

        if amount % coin == 0:
            min_coin_count_for_that_amt_so_far = amount / coin

        if coin > amount:
            continue

        min_coin_count = coin_change_recursive(coins=coins, amount=amount - coin)
        if min_coin_count == -1:
            continue

        min_coin_count_for_that_amt_so_far = min(min_coin_count_for_that_amt_so_far, min_coin_count)
        min_coin_matching_amt = min_coin_matching_amt + min_coin_count_for_that_amt_so_far

    return min_coin_count_for_that_amt_so_far + 1 if min_coin_count_for_that_amt_so_far != float('inf') else -1


def coin_change_with_repitition(coins: list, amount: int) -> int:

    dp = np.zeros(shape=(len(coins) + 1, amount + 1))
    dp1 = np.zeros(shape=amount + 1)
    dp[:, :] = float("inf")
    dp[:, 0] = [0] * (len(coins) + 1)
    dp1[0] = float("inf")

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            coin_index = i - 1
            coin = coins[coin_index]

            amt = j
            no_of_coins = int(int(amt / coin) if (amt / coin) >= 1 else 0)
            remaining_amt = amt - (no_of_coins * coin)
            dp[i, j] = min(int(no_of_coins + dp[i - 1][remaining_amt]), dp[i - 1][j])
            dp1[j] = min(int(no_of_coins + dp1[remaining_amt]), dp1[j])

    return dp[len(coins)][amount]


if __name__ == "__main__":

    # print(coin_change([1, 2, 5], 11))
    # print(coin_change([2], 3))
    # print(coin_change([1], 0))
    # print(coin_change([2, 5, 10, 1], 27))
    print(coin_change_recursive([186, 419, 83, 408], 6249))