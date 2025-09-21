# A certain string-processing language offers a primitive operation which splits a string into two pieces.
# Since this operation involves copying the original string, it takes n units of time for a string of length n,
# regardless of the location of the cut. Suppose, now, that you want to break a string into many pieces.
# The order in which the breaks are made can affect the total running time.
# For example, if you want to cut a 20-character string at positions 3 and 10, then making the first cut at
# position 3 incurs a total cost of 20 + 17 = 37, while doing position 10 first has a better cost of 20+10 = 30.
# Give a dynamic programming algorithm that, given the locations of m cuts in a string of length n,
# finds the minimum cost of breaking the string into m + 1 pieces.


import numpy as np


def min_cost_recursive(piece_len: int, no_of_pieces: int) -> int:

    cost = piece_len
    if no_of_pieces == 1:
        return 0

    if ((piece_len / 2) == 0):
        return cost

    remaining_piece_len = int((piece_len / 2) if ((piece_len / 2) % 2 == 0) else (piece_len / 2) + 1)
    remaining_pieces_cost = min_cost_recursive(piece_len=remaining_piece_len, no_of_pieces=no_of_pieces - 1)

    return cost + remaining_pieces_cost

def spliting_cost(P, n):
    P = [0,] + P + [n,]  # make sure pos list contains both ends of string
    m = len(P)
    P = [0,] + P  # both C and P are 1-base indexed for easy reading
    C = np.full((m+1,m+1), np.inf)
    for i in range(1, m+1): C[i, i:i+2] = 0  # any segment <= 2 does not need split so is zero cost
    for s in range(2, m):  # s is split string len
        for i in range(1, m-s+1):
            j = i + s
            for k in range(i, j+1):
                C[i,j] = min(C[i,j], P[j] - P[i] + C[i,k] + C[k,j])
    return C[1,m]

if __name__ == '__main__':
    print(spliting_cost([3, 5, 10, 14, 16, 19], 20))