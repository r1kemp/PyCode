'''
    https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021
    Google - Kick Start - 2022 Round A - Problem #1
'''
def SpeedTyping():
    T = int(input())
    for t in range(1, T+1):
        S = input()
        P = input()
    
        ls = len(S)
        lp = len(P)
    
        if lp < ls:
            print(f'Case #{t}: IMPOSSIBLE')
            continue
        
        imp = False
        j = 0
        count = 0
        for i in range(len(S)):
            start = j
            while j < lp and P[j] != S[i]:
                j += 1
            
            if j == lp:
                imp = True
                break
    
            count += j - start
            if (lp - j) < (ls -i):
                imp = True
                break
    
            j += 1
            
        if imp:
            print(f'Case #{t}: IMPOSSIBLE')
        else:
            count += lp - j
            print(f'Case #{t}: {count}')


'''
    https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997
    Google - Kick Start - 2022 Round A - Problem #2
'''
def ChallengeNine():
    T = int(input())
    for t in range(1, T+1):
        ns = input()
    
        d = 0
        for s in ns:
            d += int(s)
            d %= 9
    
        if d > 0:
            d = 9 - d
    
        if d == 0:
            ans = ns[0] + '0' + ns[1:]
            print(f'Case #{t}: {ans}')
            continue
        if d == 1:
            ans = '1' + ns
            print(f'Case #{t}: {ans}')
            continue
        
        ds = str(d)
        done = False
        for i in range(len(ns)):
            if ds < ns[i]:
                ans = ns[:i] + ds + ns[i:] 
                print(f'Case #{t}: {ans}')
                done = True
                break
    
        if not done:
            ans = ns + ds
            print(f'Case #{t}: {ans}')
    

