'''
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2
Round C 2020 - Kick Start 2020
'''

'''
Problem #1: Countdown
'''

def Countdown():
    T = int(input())
    for t in range(1, T+1):
        N, K = (int(x) for x in input().split(' '))
        A = [int(x) for x in input().split(' ')]
        
        ans = 0
        countdown_started = False
    
        for i in range(N):
            if countdown_started:
                if A[i] != A[i-1] - 1:
                    countdown_started = False
                elif A[i] == 1:
                    ans += 1
                    countdown_started = False
                else:
                    continue
            if A[i] == K:
                countdown_started = True
    
        print(f'Case #{t}: {ans}')


'''
Problem #3: Perfect Subarray
Status: TLE
'''
from itertools import accumulate

def PerfectSubarray():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        A = [int(x) for x in input().split(' ')]
        B = [0] + [x for x in accumulate(A)]
        sqs = {x * x:None for x in range(3165)}
    
        ans = 0
        for a in A:
            if a in sqs:
                ans += 1
        
        for i in range(N):
            for j in range(i+2, N + 1):
                sub_array_sum = B[j] - B[i] 
                if sub_array_sum in sqs:
                    ans += 1
    
        print(f'Case #{t}: {ans}')


'''
Problem #4: Candies
'''

class FenwickTree:
    def __init__(self, A) -> None:
        self._ft = [0] * (len(A) + 1) #internally we use 1-based index
        
        for i in range(len(A)):
            self.increment(i, A[i])

    def increment(self, i, by):
        i += 1      #internally we use 1-based index

        while i < len(self._ft):
            self._ft[i] += by
            i += (i & (-i))

    # [start, end] 
    def rangeSum(self, start, end):
        endSum = self.prefixSum(end)
        if start == 0:
            return endSum
        
        minusSum = self.prefixSum(start - 1)
        return endSum - minusSum

    def prefixSum(self, i):
        i += 1      #internally we use 1-based index

        pxSum = 0
        while i > 0:
            pxSum += self._ft[i]
            i -= (i & (-i))

        return pxSum

def Candies():
    T = int(input())
    for t in range(1, T+1):
        N, Q = (int(x) for x in input().split(' '))
        A = [int(x) for x in input().split(' ')]
        ps1 = [(-1)**p * x for p,x in enumerate(A)]
        ps2 = [(-1)**p * (p+1) * x for p,x in enumerate(A)]
    
        ft1 = FenwickTree(ps1)
        ft2 = FenwickTree(ps2)
    
        final_ans = 0
    
        for _ in range(Q):
            line = input()
            if line[0] == 'Q':
                left, right = (int(x) for x in line[2:].split(' '))
                left -= 1
                right -= 1
                temp_1 = ft1.rangeSum(left, right)
                temp_2 = ft2.rangeSum(left, right)
    
                ans = temp_2 - left * temp_1
                if left % 2 == 1:
                    ans *= -1
                # print(f'*******  {line} = {ans}')
    
                final_ans += ans
    
            if line[0] == 'U':
                index, val = (int(x) for x in line[2:].split(' '))
                index -= 1
                val1 = (-1)**index * val
                ft1.increment(index, val1 - ps1[index])
                ps1[index] = val1
    
                val2 = (-1)**index * (index + 1) * val
                ft2.increment(index, val2 - ps2[index])
                ps2[index] = val2
    
                A[index] = val
                # print(f'*******  {line} = {A}')
                
        print(f'Case #{t}: {final_ans}')

