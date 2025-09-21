# A subsequence is palindromic if it is the same whether read left to right or right to left.
# For instance, the sequence
# A,C,G,T,G,T,C, A, A, A, A,T,C,G
# has many palindromic subsequences, including A, C , G , C , A and A, A, A, A (on the other hand,
# the subsequence A, C , T is not palindromic).
# Devise an algorithm that takes a sequence x[1 . . . n] and returns the (length of the) longest palindromic
# subsequence. Its running time should be O(n2)

import numpy as np

def longest_palindromic(str_arr: list) -> int:

    str_len = len(str_arr)
    dp = np.zeros(shape=(str_len, str_len))

    for i in range(str_len - 1, -1, -1):

        dp[i][i] = 1

        for j in range(i + 1, str_len):
            s_i = str_arr[i]
            s_j = str_arr[j]
            if s_i == s_j:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return int(dp[0][str_len - 1])