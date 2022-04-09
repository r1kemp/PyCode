'''
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8
Round B 2020 - Kick Start 2020
'''
# Problem #1: Bike Tour
def BikeTour():
    for t in range(1, 1 + int(input())):
        n = int(input())
        h = [int(x) for x in input().split(' ')]
        pks = 0
        for i in range(1, n-1):
            if h[i-1] < h[i] and h[i] > h[i+1]:
                pks += 1
        print(f'Case #{t}: {pks}')

    
# Problem #2: Bus Routes
def BusRoutes():
T = int(input())
for t in range(1, T + 1):
    N, D = (int(x) for x in input().split(' '))
    X = [int(x) for x in input().split(' ')]
    E = D
    for x in reversed(X):
        E -= E % x
    print(f'Case #{t}: {E}')


# Problem #3: Robot Path Decoding
def ensure_in_range(delta):
    delta %= 10**9
    if delta < 0:
        delta += 10**9
    return delta

def RobotPathDecoding():
    for t in range(int(input())):
        moves = input()
    
        N, S, E, W = 0, 0, 0, 0
        mul_stack = []
        mul = 1
    
        for c in moves:
            if c.isdigit():
                mul_stack.append(mul)
                mul *= ord(c) - ord('0')
            elif c == 'N':  N += mul
            elif c == 'S':  S += mul
            elif c == 'E':  E += mul
            elif c == 'W':  W += mul
            elif c == ')':  mul = mul_stack.pop()
            else:
                pass
    
        delta_h = ensure_in_range(E - W)
        delta_w = ensure_in_range(S - N)
    
        print(f'Case #{t + 1}: {1 + delta_h} {1 + delta_w}')
            
    


# Problem #4: Wandering Robot
from math import log2
from math import pow
from itertools import accumulate

def WanderingRobot():
    T = int(input())
    for t in range(1, T+1):
        W, H, L, U, R, D = (int(x) for x in input().split(' '))
        W, H, L, U, R, D = W-1, H-1, L-1, U-1, R-1, D-1
    
        logs_of_facs = [0] + [x for x in accumulate(log2(y) for y in range(1, W+H))]
    
        prob = 0
    
        if R < W:
            for h in range(U):
                log_p = logs_of_facs[h + R] - logs_of_facs[h] - logs_of_facs[R] - h - R
                prob += pow(2, log_p)
            
        if D < H:
            for w in range(L):
                log_p = logs_of_facs[w + D] - logs_of_facs[w] - logs_of_facs[D] - w - D
                prob += pow(2, log_p)
    
        prob *= 0.5
    
        print(f'Case #{t}: {prob}')
    

