'''
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3
Round A 2020 - Kick Start 2020
'''

# Problem #1: Allocation
def Allocation():
    T = int(input())
    for t in range(1, T+1):
        N, B = (int(x) for x in input().split(' '))
        A = [int(x) for x in input().split(' ') if int(x) <= B]
        A.sort()
        curCount = 0
        curTot = 0
        for a in A:
            curTot += a
            if curTot > B:
                break
            curCount += 1
        print(f"Case #{t}: {curCount}")
        

# Problem #2: Plates
def Plates():
    T = int(input())
    for t in range(1, T+1):
        N, K, P = (int(x) for x in input().split(' '))
        S = []
        for _ in range(N):
            s_i = [int(x) for x in input().split(' ')]
            if P < K:
                s_i = s_i[:P]
    
            s_i = [0] + s_i
    
            for i in range(1, len(s_i)):
                s_i[i] += s_i[i-1]
            S.append(s_i)
            
        dp = [0] * (P + 1)
        if P < K:
            K = P
        for i in range(K + 1):
            dp[i] = S[0][i]
    
        dp2 = [0] * (P+ 1)
    
        for i in range(1, N):
            for p in range(1, P+1):
                left, right = p, 0
                while left >= 0 and right <= K:
                    val = dp[left] + S[i][right]
                    dp2[p] = max(dp2[p], val)
                    left -= 1
                    right += 1
    
            dp, dp2 = dp2, dp
    
        print(f'Case #{t}: {dp[P]}')
    
    
# Problem #3: Workout
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

def Workout():
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


#Problem #4: Bundling
def Bundling():
    for t in range(1, int(input()) + 1):
        N, K = (int(x) for x in input().split(' '))
    
        sarr = []
        smax = 0
        for _ in range(N):
            s = input()
            sarr.append(s)
            smax = max(smax, len(s))
    
        sarr.sort()
    
        match = [1] * len(sarr[0])
        match += [0] * (smax - len(sarr[0]))
    
        ans = 0
    
        for i in range(1, N):
            prev_str_len = len(sarr[i-1])
            curr_str_len = len(sarr[i])
            min_len = min(curr_str_len, prev_str_len)
            max_len = max(curr_str_len, prev_str_len)
    
            j = 0
            while j < min_len and sarr[i][j] == sarr[i-1][j]:
                match[j] += 1
                j += 1
            
            for p in range(j, max_len):
                if match[p] < K: break
    
                while match[p] >= K:
                    ans += 1
                    match[p] -= K
    
            while j < curr_str_len:
                match[j] = 1
                j += 1
    
            while j < max_len:
                match[j] = 0
                j += 1
    
        for p in range(max_len):
            if match[p] < K: break
    
            while match[p] >= K:
                ans += 1
                match[p] -= K
    
    
        print(f"Case #{t}: {ans}")

