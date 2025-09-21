'''
DPV 6.13.
Consider the following game. A dealer produces a sequence s1..sn of cards, face up, where
 each card si has a value vi. Then two players take turns picking a card from the sequence,
but can only pick the first or the last card of the (remaining) sequence. The goal is to collect
cards of largest total value. (For example, you can think of the cards as bills of different denominations.)
Assume n is even.
    (a) Show a sequence of cards such that it is not optimal for the first player to start by picking
        up the available card of larger value. That is, the natural greedy strategy is suboptimal.
    (b) Give an O(n2) algorithm to compute an optimal strategy for the first player. Given the
        initial sequence, your algorithm should precompute in O(n2) time some information, and
        then the rst player should be able to make each move optimally in O(1) time by looking
        up the precomputed information.

Solution/Solution approach:
(a) Lets take an example sequence 10, 100, 1, 1. Here if the first player selects 10 (comparing 1 and 10) then The second player
    will select 100 and win. Instead, if the first player selects the last card of value 1, then the second player will choose
    either 10 or 1 and first player will be able to select 100 to win.

(b)


'''
import numpy as np

def cardGame(S):
    '''
        Arguements:
    '''
    n = len(S)
    M = np.array([[0 for x in range(n + 1)] for x in range(n + 1)])
    for i in range(n):
        M[i, i] = S[i]

    for i in range(0, n):
        for j in range(n):
            if (i < j):
                si = S[i] - M[i + 1][j]
                sj = S[j] - M[i][j - 1]
                M[i][j] = max(si, sj)
                print()

    return M[0, n - 1]


def main():
    s = [10, 100, 1, 1]

    print
    cardGame(s)


if __name__ == '__main__':
    s = [10, 100, 1, 1]

    print(cardGame(s))