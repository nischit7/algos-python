# Given two strings x = x1x2 ···xn and y = y1y2 ···ym, we wish to find the length of their longest common substring,
# that is, the largest k for which there are indices i and j with xixi+1 ···xi+k−1 = yj yj+1 ···yj+k−1.
# Show how to do this in time O(mn).

import numpy as np

def longest_common(s1: str, s2: str) -> int:

    dp = np.zeros(shape=(len(s1), len(s2)))

    for i in range(len(s1)):

        for j in range(len(s2)):

            if s1[i] == s2[j]:
                dp[i][j] = ((dp[i - 1][j - 1]) if (i - 1) >= 0 and (j - 1) >= 0 else 0) + 1
            else:
                dp[i][j] = max(dp[i][j - 1] if (j - 1) >= 0 else 0, dp[i - 1][j] if (i - 1) >= 0 else 0)

    return int(dp[len(s1) - 1][len(s2) - 1])