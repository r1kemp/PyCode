'''
 Round F 2020 - Kick Start 2020
 https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48
'''

'''
Problem #1: ATM Queue
'''
from collections import defaultdict
from math import ceil
    
def ATMQueue():
    T = int(input())
    for t in range(1, T+1):
        N, X = (int(x) for x in input().split(' '))
        A = [int(x) for x in input().split(' ')]
    
        D = [None]*N
        for i in range(N):
            D[i] = (ceil(A[i]/X), str(i + 1))
        
        D.sort(key=lambda P: P[0])
        ans_lst = [P[1] for P in D]
    
        ans_lst = ' '.join(ans_lst)
        print(f'Case #{t}: {ans_lst}')
    
#ATMQueue()

'''
Problem #2: Painters' Duel
'''
def rptobit(r, p):
    ar = [0, 0, 1, 4, 9, 16, 25, 36, 49, 64]
    return 1 << (ar[r] + p)

def CalcScoreForBerthesTurn(M, ra, pa, rb, pb, ca, cb, callAlma=True):
    score = 100
    BertheMoved = False

    left = pb - 1
    if left > 0:
        bit = rptobit(rb, left)
        if M & bit:
            score = CalcScoreForAlmasTurn(M ^ bit, ra, pa, rb, left, ca, cb+1)
            BertheMoved = True

    right = pb + 1
    if right < (2 * rb):
        bit = rptobit(rb, right)
        if M & bit:
            score2 = CalcScoreForAlmasTurn(M ^ bit, ra, pa, rb, right, ca, cb+1)
            score = min(score, score2)
            BertheMoved = True

    bottom = rb+1
    if pb % 2 == 1 and bottom <= S:
        bit = rptobit(bottom, right)
        if M & bit:
            score2 = CalcScoreForAlmasTurn(M ^ bit, ra, pa, bottom, right, ca, cb+1)
            score = min(score, score2)
            BertheMoved = True
            
    top = rb-1
    if pb % 2 == 0 and top > 0:
        bit = rptobit(top, left)
        if M & bit:
            score2 = CalcScoreForAlmasTurn(M ^ bit, ra, pa, top, left, ca, cb+1)
            score = min(score, score2)
            BertheMoved = True

    if BertheMoved:
        return score
    elif callAlma:
        return CalcScoreForAlmasTurn(M, ra, pa, rb, pb, ca, cb, False)
    else:
        return ca - cb

def CalcScoreForAlmasTurn(M, ra, pa, rb, pb, ca, cb, callBerthe=True):
    score = -100
    AlmaMoved = False

    left = pa - 1
    if left > 0:
        bit = rptobit(ra, left)
        if M & bit:
            score = CalcScoreForBerthesTurn(M ^ bit, ra, left, rb, pb, ca+1, cb)
            AlmaMoved = True

    right = pa + 1
    if right < (2 * ra):
        bit = rptobit(ra, right)
        if M & bit:
            score2 = CalcScoreForBerthesTurn(M ^ bit, ra, right, rb, pb, ca+1, cb)
            score = max(score, score2)
            AlmaMoved = True

    bottom = ra+1
    if pa % 2 == 1 and bottom <= S:
        bit = rptobit(bottom, right)
        if M & bit:
            score2 = CalcScoreForBerthesTurn(M ^ bit, bottom, right, rb, pb, ca+1, cb)
            score = max(score, score2)
            AlmaMoved = True
            
    top = ra-1
    if pa % 2 == 0 and top > 0:
        bit = rptobit(top, left)
        if M & bit:
            score2 = CalcScoreForBerthesTurn(M ^ bit, top, left, rb, pb, ca+1, cb)
            score = max(score, score2)
            AlmaMoved = True

    if AlmaMoved:
        return score
    elif callBerthe:
        return CalcScoreForBerthesTurn(M, ra, pa, rb, pb, ca, cb, False)
    else:
        return ca - cb


def PaintersDuel():
    T = int(input())
    for t in range(1, T+1):
        S, ra, pa, rb, pb, C = (int(x) for x in input().split(' '))
    
        N = S * S
        M = 2**(N+1) - 2
    
        M ^= rptobit(ra, pa)
        M ^= rptobit(rb, pb)
    
        for i in range(C):
            r, p = (int(x) for x in input().split(' '))
            M ^= rptobit(r, p)
            
        ans = CalcScoreForAlmasTurn(M, ra, pa, rb, pb, 1, 1)
    
        print(f'Case #{t}: {ans}')
    


