'''
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed
Round E 2020 - Kick Start 2020
Problem #1: Longest Arithmetic    
'''
def LongestArithmetic():
T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = [int(x) for x in input().split(' ')]

    max_count = 0
    prev_diff = A[1] - A[0] + 1 
    curr_count = 0
    
    for i in range(1, N):
        diff = A[i] - A[i-1]
        if diff == prev_diff:
            curr_count += 1
        else:
            max_count = max(max_count, curr_count)
            prev_diff = diff
            curr_count = 2
    
    
    max_count = max(max_count, curr_count)
    print(f'Case #{t}: {max_count}')


'''
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bede9
Round E 2020 - Kick Start 2020
Proble #3: Toys
'''
import heapq
class PriorityQueue(object):
    def __init__(self) -> None:
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def peek(self):
        return self._queue[0][2]

    def size(self):
        return len(self._queue)


def Toys():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        E = [0] * N
        R = [0] * N
        S = [0] * N
        eSum = 0
    
        for i in range(N):
            E[i], R[i] = (int(x) for x in input().split(' '))
            S[i] = E[i] + R[i]
    
            eSum += E[i]
    
        if N == 1:
            duration = E[0] if R[0] else 'INDEFINITELY'
            print(f'Case #{t}: {duration} 0')
            continue
                
        q = PriorityQueue()
        popCount = 0
        ans = eSum, 0  # maxEnjoyment, popCount
        currEnj = eSum
    
    
        for i in range(N):
            q.push((S[i], E[i]), S[i])
            currEnj += E[i]
    
            while q.size() > 0 and q.peek()[0] > eSum:
                tmp = q.pop()
                popCount += 1
                eSum -= tmp[1]
                currEnj -= 2 * tmp[1]
    
            if currEnj > ans[0]:
                ans = currEnj, popCount
    
        if q.size() == 0:
            print(f'Case #{t}: {ans[0]} {ans[1]}')
        else:
            popCount = N - q.size()
            print(f'Case #{t}: INDEFINITELY {popCount}')
    

