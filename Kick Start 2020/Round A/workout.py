# 
#  https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b
#
#  https://github.com/kamyu104/GoogleKickStart-2020
#

def read_ints():
    return (int(x) for x in input().split(' '))

def read_ints_list():
    return [int(x) for x in input().split(' ')]

import math
def cuts(M, N, sz):
    ans = 0
    for i in range(N):
        if M[i] > sz:
            ans += math.ceil(M[i] / sz) - 1

    return ans

def binary_srch(M, N, K, lo, hi):
    mid = (lo + hi) // 2
    if mid == lo:
        cuts_lo = cuts(M, N, lo)
        if cuts_lo <= K:
            return lo
        else:
            return hi

    cuts_req = cuts(M, N, mid)

    if cuts_req > K:
        lo = mid
    else:
        hi = mid
    
    return binary_srch(M, N, K, lo, hi)

T, = read_ints()

for t in range(1, T+1):
    N, K = read_ints()
    M = read_ints_list()

    max_diff = 0
    for i in range(N-1):
        M[i] = M[i+1] - M[i]
        max_diff = max(max_diff, M[i])

    opt = binary_srch(M, N-1, K, 1, max_diff)
    print(f"Case #{t}: {opt}")





