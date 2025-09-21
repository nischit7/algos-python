import numpy as np
import sys
def coin_change_no_repitition(coins: list, amount: int) -> bool:
    dp = np.zeros(shape=(len(coins) + 1, amount + 1))
    dp[:, :] = 0
    dp[:, 0] = [0] * (len(coins) + 1)

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            coin_index = i - 1
            coin = coins[coin_index]

            amt = j
            no_of_coins = 1 if (amt >= coin) >= 1 else 0
            remaining_amt = amt - (no_of_coins * coin)
            dp[i, j] = (no_of_coins * coin) + dp[i - 1][remaining_amt]

    return dp[len(coins)][amount] == amount


if __name__ == "__main__":

    # print(coin_change([1, 2, 5], 11))
    # print(coin_change([2], 3))
    # print(coin_change([1], 0))
    # print(coin_change([2, 5, 10, 1], 27))
    print(coin_change_no_repitition([186, 419, 83, 408], 6249))